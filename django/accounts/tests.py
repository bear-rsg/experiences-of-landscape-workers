from django.test import TestCase
from django.urls import reverse


class TestAccountTemplateView(TestCase):
    """
    Test Account View
    """
    def test_account_template_empty_get(self):
        """
        Test the simple account page is returned
        """
        url = reverse('account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Account')

    def test_account_template_nonempty_get(self):
        """
        Test the simple account page is returned
        """
        url = reverse('account')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Account')
