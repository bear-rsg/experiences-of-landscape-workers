/*
    This file displays a popup message to users about the website's cookies policy

    This is a self-contained file (includes HTML, CSS, JS) so that it can be easily added to any project.
    Ensure any links in the generated HTML point to a valid URL for the website it's being used in (e.g. the cookies page)

    Requires:
        - jQuery
        - cookie plugin for jQuery: https://plugins.jquery.com/cookie/
*/

$(document).ready(function() {

    // If user has not previously hidden the cookie message, then show it
    if($.cookie("cookie_msg_hide") != "1")
    {
        // Build html of the cookies message box
        var html = `
<div id="cookiemsg" style="text-align: center; z-index: 10000; background: black; width: 96vw; padding: 1em; color: white; position: fixed; bottom: 2vw; right: 2vw;">
    <i class="fas fa-cookie-bite"></i> 
    We use cookies to enhance this website. See our <a href="/cookies/" style="color: white; text-decoration: underline;">cookies policy</a> for more information.
    <span id="cookiemsg-hide" style="display: inline-block; background: white; color: black; padding: 0.4em 1.7em; margin-left: 1em; cursor: pointer; vertical-align: middle;">
        Hide
    </span>
</div>    
        `;
    
        // Add the html to the body of the page
        $('body').append(html);
    }
   
    // When user clicks button to hide cookie message
    $('#cookiemsg-hide').on('click', function(){
        
        // Set cookie val to True (1)
        $.cookie("cookie_msg_hide", "1", { expires: 1000, path: '/'});

        // Hide cookie message box
        $('#cookiemsg').hide();

    });

});