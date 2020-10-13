from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .views import XMLImporterProcessView


class TestConstructionListView(TestCase):
    """
    Test Construction List View
    """
    def test_construction_list_empty_get(self):
        """
        Test the construction list page is returned
        """
        url = reverse('construction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'English Constructicon')
        self.assertContains(response, 'Search')

    def test_construction_list_nonempty_get(self):
        """
        Test the construction list page is returned
        """
        url = reverse('construction-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'English Constructicon')
        self.assertContains(response, 'Search')

    def test_construction_list_nonsense_post(self):
        """
        Nonsense POST request of the construction list page
        should error 405, as POST is not allowed
        """
        url = reverse('construction-list')
        response = self.client.post(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 405)


class TestConstructionDetailView(TestCase):
    """
    Test Construction Detail View
    """

    fixtures = ['test.json', ]

    def test_construction_detail_empty_get(self):
        """
        Test the construction detail page is returned
        """
        url = reverse('construction-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'English Constructicon')
        self.assertContains(response, 'Form')

    def test_construction_detail_nonempty_get(self):
        """
        Test the construction detail page is returned
        """
        url = reverse('construction-detail', kwargs={'pk': 1})
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'English Constructicon')
        self.assertContains(response, 'Form')

    def test_construction_detail_nonsense_post(self):
        """
        Nonsense POST request of the construction detail page
        should error 405, as POST is not allowed
        """
        url = reverse('construction-detail', kwargs={'pk': 1})
        response = self.client.post(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 405)


class TestXMLImporterProcessView(TestCase):
    """
    Test XML Importer Process View
    """
    def setUp(self):
        """
        Set up test data to be used by test methods
        """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testusername', email='testemail@testdomain.com', password='testpassword')

    def test_xml_importer_process_view_empty_get(self):
        """
        Test the construction detail page is returned
        """
        url = reverse('import-process')
        request = self.factory.get(url)
        request.user = self.user
        response = XMLImporterProcessView(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'English Constructicon')
        self.assertContains(response, 'Success')
