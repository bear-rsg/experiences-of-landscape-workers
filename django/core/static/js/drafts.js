$(document).ready(function () {
    //
    // Cookie functions: get, set, delete
    //

    // Get cookie value by name
    function getCookie(name) {
        // Convert cookies string to list
        var c_list = document.cookie.split("; "),
            i = 0,
            c,
            c_name,
            c_value;
        // Loop through cookies list to find a match
        for (i = 0; i < c_list.length; i++) {
            // Find cookie
            c = c_list[i].split("=");
            c_name = c[0];
            c_value = c[1];
            // Return cookie value if cookie name matches
            if (c_name === name) {
                return c_value;
            }
        }
        // If no cookie found with given name, return null
        return null;
    }

    // Set cookie value by name
    function setCookie(name, value) {
        document.cookie = name + "=" + value + "; path=/;";
    }

    // Delete cookie by name
    function deleteCookie(name) {
        document.cookie =
            name + "=0; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    }

    //
    // General Functions
    //

    // Tidy date
    function tidyDate(date) {
        return String(new Date(parseInt(date))).substring(0, 21);
    }

    // Shorten with elipses if needed
    function truncate(string, length) {
        return string.length <= length
            ? string
            : string.substring(0, length) + "...";
    }

    //
    // Drafts
    //

    // Define the 'drafts' database
    var db = new Dexie("db_drafts");
    // Version 1: store 'name' (acts as PK) and 'text'
    db.version(1).stores({
        drafts: "name,text",
    });

    // Load current draft in 'create journal entry' form
    $("#drafteditor-buttons").on(
        "click",
        "#drafteditor-buttons-addtojournal",
        function () {
            // Must be editing an existing draft and be online
            if (navigator.onLine) {
                if (getCookie("currentDraft")) {
                    // Get cleaned text
                    var txt = $.trim($("#drafteditor-text").val());
                    // Save progress of current draft
                    db.drafts
                        .put({ name: getCookie("currentDraft"), text: txt })
                        .then(function () {
                            return db.drafts.get(getCookie("currentDraft"));
                        })
                        .then(function (draft) {
                            // Set currentDraft cookie
                            setCookie("currentDraft", draft.name);
                            // Go to journal
                            window.location.assign("/journal/create/");
                        });
                } else {
                    alert(
                        "Cannot load draft. Please try saving your draft and restarting this app."
                    );
                }
            } else {
                alert(
                    "Oops, it looks like you're offline. Please try again when you have an internet connection."
                );
            }
        }
    );

    // Save current draft
    $("#drafteditor-buttons").on(
        "click",
        "#drafteditor-buttons-save",
        function () {
            dt = Date.now();
            var txt = $.trim($("#drafteditor-text").val());

            // Draft text can't be empty when saving
            if (txt !== "") {
                // If a draft is currently being edited, update it. Otherwise add new draft using current timestamp
                var draftname = getCookie("currentDraft")
                    ? getCookie("currentDraft")
                    : String(dt);

                // Save draft (automatically knows whether to update/add new based on matching name)
                db.drafts
                    .put({ name: draftname, text: txt })
                    .then(function () {
                        return db.drafts.get(draftname);
                    })
                    .then(function (draft) {
                        // Delete currentDraft cookie
                        deleteCookie("currentDraft");
                        // Refresh page
                        window.location.assign(
                            window.location.pathname + "#mydrafts-title"
                        );
                    });
            } else {
                alert("Draft is empty");
            }
        }
    );

    // Delete current draft
    $("#drafteditor-buttons").on(
        "click",
        "#drafteditor-buttons-delete",
        function () {
            if (getCookie("currentDraft")) {
                db.drafts
                    .delete(getCookie("currentDraft"))
                    .then(function (currentDraft) {
                        // Delete currentDraft cookie
                        deleteCookie("currentDraft");
                        // Refresh page
                        window.location.assign(window.location.pathname);
                    });
            }
        }
    );

    // Delete current draft when submitting journal entry
    $("#journalentry-create-form").on("submit", function () {
        //If journal entry came from a draft, delete the draft
        if (getCookie("currentDraft")) {
            db.drafts.delete(getCookie("currentDraft"));
        }
    });

    // List current drafts
    db.drafts.count().then(function (c) {
        // Only show if there are drafts
        if (c > 0) {
            items = "";
            db.drafts
                .each(function (draft) {
                    items +=
                        `<div class="drafts-list-item">
                                                <a href="#drafteditor-title" class="drafts-list-item-link" id="` +
                        draft.name +
                        `">` +
                        tidyDate(draft.name) +
                        `</a><p>` +
                        truncate(draft.text, 30) +
                        `</p></div>`;
                })
                .then(function () {
                    html = `<div id="drafts-list">` + items + `</div>`;
                    $("#mydrafts").html(html);
                });
        }
    });

    // Clear currentDraft cookie each time a page is navigated to via the navigation buttons
    $(".nav-item").on("click", function () {
        deleteCookie("currentDraft");
    });

    // Clicking on a draft in the list
    $("#mydrafts").on("click", ".drafts-list-item-link", function () {
        // Set this draft (based on its id) as the currentDraft
        setCookie("currentDraft", $(this).prop("id"));

        // Load current draft text into text editor
        if (getCookie("currentDraft")) {
            db.drafts.get(getCookie("currentDraft")).then(function (currentDraft) {
                setDraftEditorState();
                $("#drafteditor-text").val(currentDraft.text);
            });
        }
    });

    // Load current draft text into text area
    if (getCookie("currentDraft")) {
        db.drafts
            .get(getCookie("currentDraft"))
            .then(function (currentDraft) {
                $("#id_entry_text, #drafteditor-text").val(currentDraft.text);
            })
            .catch(function (error) {
                console.log("Expected error: " + error);
            });
    }

    // Show pending drafts alert to user
    var pagesToExcludeAlerts = ["/journal/drafts/", "/journal/create/"];
    var currentUrl = window.location.pathname;
    // If online and current URL isn't in above exclude list
    if (navigator.onLine && !pagesToExcludeAlerts.includes(currentUrl)) {
        // If there are drafts yet to be submitted
        db.drafts.count().then(function (c) {
            if (c > 0) {
                // Show the message
                html_drafts = `<a href="/journal/drafts/">Tap here to complete your drafts</a>`;
                $("#main-alerts").html(html_drafts).slideDown("fast");
            }
        });
    }

    function setDraftEditorState() {
        // Set the draft editor into create/edit state based on whether a draft is being edited or not

        // Change text label
        // If a currentDraft cookie exists, load it into
        if (getCookie("currentDraft"))
            var label = "Edit draft:- " + tidyDate(getCookie("currentDraft"));
        else var label = "Create a draft:";
        // Apply HTML
        $("#drafteditor-text-label").html(label);

        // Change the action buttons
        if (getCookie("currentDraft")) {
            var buttons = `<button id="drafteditor-buttons-save" type="submit" class="btn btn-primary"><i class="fas fa-pen"></i> Save Changes</button>`;
            // If online, give option to add to journal
            if (navigator.onLine) {
                buttons += `<button id="drafteditor-buttons-addtojournal" class="btn btn-primary"><i class="fas fa-plus-circle"></i> Add To Journal</button>`;
            }
            buttons += `<button id="drafteditor-buttons-delete" class="btn btn-danger"><i class="fas fa-trash-alt"></i> Delete</button>`;
        } else {
            var buttons = `<button id="drafteditor-buttons-save" type="submit" class="btn btn-primary"><i class="fas fa-pen"></i> Create Draft</button>`;
        }
        // Apply HTML
        $("#drafteditor-buttons").html(buttons);
    }

    setDraftEditorState();
});
