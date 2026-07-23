import pytest
from playwright.sync_api import sync_playwright
import os
from playwright.sync_api import Page
from dotenv import load_dotenv
from pages.web.login_page import LoginPage
from pages.web.home_page import HomePage
from pages.web.sign_up_page import SignUpPage
load_dotenv()

@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(
          headless=True
          )
       yield browser
       browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        reduced_motion="reduce",
    )

    context.add_init_script("""
        document.addEventListener("DOMContentLoaded", () => {
            const style = document.createElement("style");
            style.textContent = `
                *, *::before, *::after {
                    animation-duration: 0s !important;
                    animation-delay: 0s !important;
                    transition-duration: 0s !important;
                    transition-delay: 0s !important;
                    scroll-behavior: auto !important;
                }

                .reveal, .reveal.visible {
                    opacity: 1 !important;
                    transform: none !important;
                }
            `;
            document.head.appendChild(style);
        });
    """)

    test_page = context.new_page()
    yield test_page
    context.close()
   
@pytest.fixture
def login_page(page:Page):
   page.goto(os.environ["LOGIN_URL"])
   return LoginPage(page)

@pytest.fixture
def sign_up_page(page:Page):
   page.goto(os.environ["JOIN_URL"])
   return SignUpPage(page)

@pytest.fixture
def home_page(page:Page):
   page.goto(os.environ["BASE_URL"])
   return HomePage(page)
    