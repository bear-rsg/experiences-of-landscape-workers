$(document).ready(function () {

    // Submit journal entry form
    $('#journalentry-form-submit').on('click', function(e) {                
        // If form mandatory text is present
        if ($("#id_entry_text").val() != '') {
            // Stop form from submitting
            e.preventDefault();

            // If can connect to the internet
            if(navigator.onLine) {
                // Show loading screen
                $('.loading-container').show();
                $('html, body').css('overflow', 'hidden');
                // Articificially add a split second for the loading screen
                setTimeout(function () {
                    $('#journalentry-form').submit();    
                }, 640);
            }
            // If cannot connect to the internet
            else {
                alert(`No internet connection found.

Please try again when you have a connection or in the meantime, you can save this journal entry as a Draft`);
            }
        }
        // If manadatory text is not present
        else {
            alert(`You need to supply text for each journal entry you upload.
            
If the focus of your entry is an image, please use the text box to provide a quick description of the image.`);
        }
    });

});