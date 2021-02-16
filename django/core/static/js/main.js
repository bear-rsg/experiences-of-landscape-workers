$(document).ready(function () {
    
    //
    // Generic Functions
    //

    // Get URL
    function getUrlParameter(sParam) {
        var sPageURL = decodeURIComponent(window.location.search.substring(1)),
            sURLVariables = sPageURL.split("&"),
            sParameterName,
            i;

        // Store the value outside of loop, so if multiple of the same param name the last is taken
        var lastValueFound;

        // Loop through each parameter
        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split("=");
            if (sParameterName[0] === sParam)
                lastValueFound =
                    sParameterName[1] === undefined ? true : sParameterName[1];
        }

        return lastValueFound;
    }

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

    // If a draft has been selected (e.g. for editing) then get its name/PK from URL
    var currentDraftName = getUrlParameter("draft");

    // Load current draft in 'create journal entry' form
    $("#add-to-journal").on("click", function () {
        // Must be editing an existing draft
        if (currentDraftName) {
            // Get cleaned text
            var txt = $.trim($("#id_entry_text").val());
            // Save progress of current draft
            db.drafts
                .put({ name: currentDraftName, text: txt })
                .then(function () {
                    return db.drafts.get(currentDraftName);
                })
                .then(function (draft) {
                    // Go to journal
                    window.location.assign("/journal/create/?draft=" + currentDraftName);
                });
        }
    });

    // Save current draft
    $("#save-draft").on("click", function () {
        dt = Date.now();
        var txt = $.trim($("#id_entry_text").val());

        // Draft text can't be empty when saving
        if (txt !== "") {
            // If a draft is currently being edited, update it. Otherwise add new draft using current timestamp
            var draftname = currentDraftName ? currentDraftName : String(dt);

            // Save draft (automatically knows whether to update/add new based on matching name)
            db.drafts
                .put({ name: draftname, text: txt })
                .then(function () {
                    return db.drafts.get(draftname);
                })
                .then(function (draft) {
                    // Refresh page
                    window.location.assign(window.location.href.split(/[?#]/)[0]);
                });
        } else {
            alert("Draft is empty");
        }
    });

    // Delete current draft
    $("#delete-draft").on("click", function () {
        if (currentDraftName) {
            db.drafts.delete(currentDraftName).then(function (currentDraft) {
                // Refresh page
                window.location.assign(window.location.href.split(/[?#]/)[0]);
            });
        }
    });

    // Delete current draft when submitting journal entry
    $("#journalentry-create-form").on("submit", function () {
        //If journal entry came from a draft, delete the draft
        if (currentDraftName) {
            db.drafts.delete(currentDraftName);
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
                                                <a href="?draft=` +
                        draft.name +
                        `#create-draft">` +
                        tidyDate(draft.name) +
                        `</a>
                                                <p>` +
                        truncate(draft.text, 30) +
                        `</p>
                                        </div>`;
                })
                .then(function () {
                    html = `<div id="drafts-list">` + items + `</div>`;
                    $("#drafts").html(html);
                });
        }
    });

    // Load current draft text into text editor
    if (currentDraftName) {
        db.drafts.get(currentDraftName).then(function (currentDraft) {
            $("#id_entry_text").val(currentDraft.text);
        });
    }

    // Show pending drafts alert to user
    var pagesToExcludeAlerts = ['/journal/drafts/', '/journal/create/'];
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

});
