import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class homeOz(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_a1_login(self):
        driver = self.driver
        driver.get("http://oz.by/")
        e = driver.find_element_by_css_selector('.top-panel__userbar__auth__lbl').click()
        e_mail = driver.find_element_by_name('cl_email')
        e_password = driver.find_element_by_name('cl_psw')
        e_mail.send_keys('code-e@programmer.net')
        e_password.send_keys('212121code')
        e_password.send_keys(Keys.RETURN)
        time.sleep(5)

    def test_a2_search_in_oz_by(self):
        driver = self.driver
        driver.get("http://oz.by/")
        self.assertIn("Доставка по Беларуси", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("самая нужная книга для самого нужного места")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No results found." not in driver.page_source

    def test_a3_open_cart(self):
        driver = self.driver
        driver.get("http://oz.by/")
        e = driver.find_element_by_css_selector('.top-panel__userbar__cart__item').click()
        time.sleep(2)

    def test_a4_show_call(self):
        driver = self.driver
        driver.get("http://oz.by/")
        e = driver.find_element_by_css_selector('.dashed').click()
        time.sleep(2)

    def test_a5_login_logout(self):
        driver = self.driver
        driver.get("http://oz.by/")
        e = driver.find_element_by_css_selector('.top-panel__userbar__auth__lbl').click()
        e = driver.find_element_by_css_selector('.authozby.i-social-buttons__link').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()