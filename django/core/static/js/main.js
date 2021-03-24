$(document).ready(function () {

    // Submit journal entry form
    $('#journalentry-form-submit').on('click', function(e) {                
        // If form mandatory text is present
        if ($("#id_entry_text").val() != '') {
            // Stop form from submitting
            e.preventDefault();
            // Show loading screen
            $('.loading-container').show();
            $('html, body').css('overflow', 'hidden');
            // Articificially add a second for the loading screen
            setTimeout(function () {
                $('#journalentry-form').submit();    
            }, 1000);
        }
        else {
            alert(`You need to supply text for each journal entry you upload.
            
If the focus of your entry is an image, please use the text box to provide a quick description of the image.`);
        }
    });

});