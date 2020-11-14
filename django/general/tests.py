from django.test import TestCase
from django.urls import reverse


class TestCookiesView(TestCase):
    """
    Test Cookies View
    """
    def test_cookies_empty_get(self):
        """
        Test the cookies page is returned
        """
        url = reverse('cookies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cookies')
        self.assertContains(response, 'For information about cookies,')

    def test_cookies_nonempty_get(self):
        """
        Test the cookies page is returned
        """
        url = reverse('cookies')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cookies')
        self.assertContains(response, 'For information about cookies,')
