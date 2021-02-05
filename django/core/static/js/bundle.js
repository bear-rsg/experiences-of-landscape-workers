(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){

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

},{}],2:[function(require,module,exports){


// Import functions
var getUrlParameter = require('./getUrlParameter');


// Initiate jQuery
$(document).ready(function() {

},{"./getUrlParameter":1}]},{},[2]);
