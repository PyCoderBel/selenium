import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class productOz(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_b1_view_full_description(self):
        driver = self.driver
        driver.get("http://oz.by/books/more10444797.html")
        e = driver.find_element_by_css_selector('.b-description__expand.i-button.i-button_full-width').click()
        time.sleep(1)

    def test_b2_image_slider(self):
        driver = self.driver
        driver.get("http://oz.by/books/more10444797.html")
        e = driver.find_element_by_css_selector('.pswipe-gallery-trigger').click()
        e = driver.find_element_by_css_selector('.pswp__button.pswp__button--arrow--right').click()
        e = driver.find_element_by_css_selector('.pswp__button.pswp__button--arrow--right').click()
        e = driver.find_element_by_css_selector('.pswp__button.pswp__button--arrow--right').click()
        e = driver.find_element_by_css_selector('.pswp__button.pswp__button--arrow--left').click()
        e = driver.find_element_by_css_selector('.pswp__button.pswp__button--arrow--left').click()
        e = driver.find_element_by_css_selector('.pswp__button.pswp__button--arrow--left').click()
        e = driver.find_element_by_css_selector('.pswp__button.pswp__button--close').click()
        time.sleep(1)

    def test_b3_add_item_to_cart(self):
        driver = self.driver
        driver.get("http://oz.by/books/more10444797.html")
        e = driver.find_element_by_css_selector('.addtocart-btn').click()
        time.sleep(1)

    def test_b4_go_comments(self):
        driver = self.driver
        driver.get("http://oz.by/books/more10444797.html")
        e = driver.find_element_by_css_selector('.b-product-title__rating-link').click()
        time.sleep(1)

    def test_b5_get_comments(self):
        driver = self.driver
        driver.get("http://oz.by/books/more10444797.html")
        e = driver.find_element_by_css_selector('.rm-review-more-link').click()
        time.sleep(1)


    def tearDown(self):
       self.driver.close()