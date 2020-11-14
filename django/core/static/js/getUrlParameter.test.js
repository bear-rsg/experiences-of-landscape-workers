const getUrlParameter = require('./getUrlParameter');


// Prepare test data

// Mock a window, as running test in command line
global.window = Object.create(window);
Object.defineProperty(window, 'location', {
value: {
	search: "?email=test@example.com&search=test search&user=12345"
}
});
// Get test values from the window.location.search using getUrlParameter 
var testValueEmail = getUrlParameter("email");
var testValueSearch = getUrlParameter("search");
var testValueUser = getUrlParameter("user");


test('The email url parameter returns the email value', () => {

	expect(testValueEmail).toBe("test@example.com");

});


test('The search url parameter returns the search value', () => {

	expect(testValueSearch).toBe("test search");

});


test('The user url parameter returns the user value', () => {

	expect(testValueUser).toBe("12345");

});
