
// Import functions
var getUrlParameter = require('./getUrlParameter');


// Initiate jQuery
$(document).ready(function() {

    // Navigation

    // Navigation toggle (on small displays)
    $('#nav-toggle').click(function(){
        if($('#nav-toggle').hasClass('nav-visible')) $('#nav-toggle, nav').removeClass('nav-visible');
        else $('#nav-toggle, nav').addClass('nav-visible');
    });

    // Hide the nav menu when a link within it is clicked (for small displays)
    $('nav ul li a').click(function(){
        $('#nav-toggle').trigger('click');
    });

    // Remove empty columns in a table
    $('table tr th').each(function(i) {
        //select all tds in this column
        var tds = $(this).parents('table')
                .find('tr td:nth-child(' + (i + 1) + ')');
        //check if all the cells in this column are empty
        if(tds.length == tds.filter(':empty').length) { 
            //hide header
            $(this).hide();
            //hide cells
            tds.hide();
        } 
    });

});