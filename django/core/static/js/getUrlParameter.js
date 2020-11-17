
// Get URL
function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    // Store the value outside of loop, so if multiple of the same param name the last is taken
    var lastValueFound;

    // Loop through each parameter
    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] === sParam) lastValueFound = sParameterName[1] === undefined ? true : sParameterName[1];
    }

    return lastValueFound;
}
// Export for testing
module.exports = getUrlParameter;
