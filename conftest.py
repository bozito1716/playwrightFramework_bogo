import pytest
from playwright.sync_api import sync_playwright
import os
from playwright.sync_api import Page
from dotenv import load_dotenv
from pages.web.login_page import LoginPage
load_dotenv()

@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       yield browser
       browser.close()

@pytest.fixture
def page(browser):
   page = browser.new_page()
   yield page
   page.close()
   
@pytest.fixture
def login_page(page:Page):
   page.goto(os.environ["LOGIN_URL"])
   return LoginPage(page)
    