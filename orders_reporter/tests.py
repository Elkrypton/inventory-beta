import unittest
from .models import *
import requests

class TestManufacturer(unittest.TestCase):
    """Manufacturer test class to test models's acceptance of new data"""

    def setUp(self):

        """
        Initiates pre-defined variables for other functions usage.
        """

        add_data = Manufacturer.objects.create(item="test", quantity=3,
                                               date_of_production='2022-12-12',
                                               sku='1000-000-0000', location='TEST-12')
        self.data = Manufacturer.objects.get(item='test')
    
    def tearDown(self):

        """
        Delete all added data through  Setup method and other test methods.
        """

        self.data.delete()

    def test_data_added(self):

        self.assertEqual(self.data.item, "test")
        self.assertEqual(self.data.quantity, 3)
        self.assertEqual(self.data.sku, '1000-000-0000')
        self.assertEqual(self.data.location, 'TEST-12')


class TestConnection(unittest.TestCase):

    """
    TestConnnection Class:
         -Tests the connection through requests to check the status codes
         -Tests that the pages are accessible.
.    """
    
    def setUp(self):

        self.root_url = "http://127.0.0.1:8000"
        self.req = requests.get(self.root_url)
        self.list_urls = ['list/','graph/','manufacturer/1/','search/','myforms/','edit_manufacturer/1/']
    
    #testing the home page root page
    def test_home_page(self):
        self.assertEqual(self.req.status_code, 200)

    #testing all the pages
    def test_all_pages(self):

        for url in self.list_urls:
            self.req = requests.get(self.root_url + '/' + url)
            self.assertEqual(self.req.status_code, 200)
    
if __name__ == "__main__":
    unittest.main()        





