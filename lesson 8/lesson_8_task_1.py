from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.FormPage import FormPage

def test_alert():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    form_page = FormPage(browser)
    form_page.get()
    form_page.enter_value()
    form_page.click_button()
    correct = form_page.is_correct_values()
    not_correct = form_page.is_not_correct_values()
    assert correct == not_correct
    
    browser.quit()