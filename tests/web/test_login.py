import os

from dotenv import load_dotenv
from playwright.sync_api import Page

from pages.web.home_page import HomePage
from pages.web.login_page import LoginPage
from utils.test_data import LoginData
load_dotenv()


#SUCCESSFUL LOGIN TEST CASE
def test_successful_login(login_page:LoginPage,page: Page):
    
    login_page.fill_email(os.environ["VALID_EMAIL"])
    login_page.fill_password(os.environ["VALID_PASSWORD"])
    login_page.click_login()
    
    page.wait_for_url("**/restaurants")
    assert "/restaurants" in page.url
    
#UNSUCCESSFUL LOGIN TEST CASE
def test_unsuccessful_login(login_page:LoginPage,page: Page):
    
    login_page.fill_email(LoginData.INVALID_EMAIL)
    login_page.fill_password(LoginData.INVALID_PASSWORD)
    login_page.click_login()
    
    login_page.wait_for_error_message()
    assert login_page.get_error_message() == "Wrong email or password."
