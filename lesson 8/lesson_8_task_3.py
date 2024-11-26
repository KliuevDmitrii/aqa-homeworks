from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage
from pages.UserDataPage import UserDataPage
from pages.OverviewPage import OverviewPage

def test_total_sum():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    login_page = LoginPage(browser)
    login_page.get()
    login_page.credentials()
    login_page.click_button()

    product_page = ProductPage(browser)
    product_page.get()
    product_page.add_product()
    product_page.click_cart()

    cart_page = CartPage(browser)
    cart_page.get()
    cart_page.click_checkout()

    user_data_page = UserDataPage(browser)
    user_data_page.get()
    user_data_page.data_entry()
    user_data_page.click_continue()
    
    overview_page = OverviewPage(browser)
    overview_page.get()
    price = overview_page.check_price_total()
    assert price == "$58.29"
    
    browser.quit()