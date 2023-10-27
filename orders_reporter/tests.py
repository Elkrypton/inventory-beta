import unittest
from .models import *
import requests

try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By

except ImportError as err:
    print("[!] Please check the following error log:\n=>:{}".format(str(err)))

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
        Delete all added data through  Setup method and other test me
        thods.
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



def test_login():
    username = "rochdi"
    password = "hardtoguess123"

    item = "selenium"
    quantity= 12
    date_of_production = "12/12/2022"
    sku = "1001-000-00001"
    location = "SEL-A1"

    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:8000/")

    driver.find_element("id", "id_username").send_keys(username)
    driver.find_element("id","id_password").send_keys(password)

    driver.find_element('id','login_btn').click()

    WebDriverWait(driver=driver, timeout=15).until(
        lambda x: x.execute_script("return document.readyState == 'complete'"))
    
   
    error_message = "correct username and password"

    errors = driver.find_elements("css selector",".errorlist.nonfield")

    for e in errors:
        print(e.text)

    if any(error_message in e.text for e in errors):
        print("Login Failed")
    else:
        print("Login was successful")
    
    driver.find_element(By.ID, "id_form").click()
    driver.find_element(By.ID,"id_item").send_keys(item)
    driver.find_element(By.ID,"id_quantity").send_keys(quantity)
    driver.find_element(By.ID,"id_date_of_production").send_keys(date_of_production)   
    driver.find_element(By.ID,"id_sku").send_keys(sku)
    driver.find_element(By.ID,"id_location").send_keys(location)
    driver.find_element(By.ID,"btn_add").click()
    
    WebDriverWait(driver=driver, timeout=15).until(
        lambda x: x.execute_script("return document.readyState == 'complete'"))
    
    print("---data was added ----")


test_login()
print("=====TESTING USING UNITTEST")
if __name__ == "__main__":

    unittest.main(warnings='ignore')





