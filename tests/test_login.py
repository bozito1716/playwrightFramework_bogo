import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bogogourmet.com/")
    page.get_by_test_id("nav-login-link").click()
    page.get_by_test_id("login-email-input").fill("admin@gmail.com")
    page.get_by_test_id("login-password-input").fill("test1234")
    page.get_by_test_id("login-submit-button").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
