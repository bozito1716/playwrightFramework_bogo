from pathlib import Path
from playwright.sync_api import Page, Locator, expect


DEFAULT_TIMEOUT = 10000

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # -------------------------
    # Navigation
    # -------------------------
    def navigate(self, url: str) -> None:
        self.page.goto(url, wait_until="networkidle")

    def refresh(self) -> None:
        self.page.reload()

    def go_back(self) -> None:
        self.page.go_back()

    # -------------------------
    # Actions
    # -------------------------
    def click(self, locator: Locator) -> None:
        self.wait_for_visible(locator)
        self.scroll_into_view(locator)
        locator.click()

    def fill(self, locator: Locator, text: str) -> None:
        self.wait_for_visible(locator)
        locator.fill(text)

    def type(self, locator: Locator, text: str) -> None:
        locator.press_sequentially(text)

    def press(self, locator: Locator, key: str) -> None:
        locator.press(key)

    def hover(self, locator: Locator) -> None:
        locator.hover()

    def double_click(self, locator: Locator) -> None:
        locator.dblclick()

    def right_click(self, locator: Locator) -> None:
        locator.click(button="right")

    def check(self, locator: Locator) -> None:
        locator.check()

    def uncheck(self, locator: Locator) -> None:
        locator.uncheck()

    def select_option(self, locator: Locator, value: str) -> None:
        locator.select_option(value)

    def scroll_into_view(self, locator: Locator) -> None:
        locator.scroll_into_view_if_needed()

    # -------------------------
    # Getters
    # -------------------------
    def get_text(self, locator: Locator) -> str:
        return locator.inner_text()

    def get_value(self, locator: Locator) -> str:
        return locator.input_value()

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()

    def is_enabled(self, locator: Locator) -> bool:
        return locator.is_enabled()

    def is_checked(self, locator: Locator) -> bool:
        return locator.is_checked()
    
    def get_current_url(self) -> str:
        return self.page.url

    # -------------------------
    # Waits
    # -------------------------
    def wait_for_visible(self, locator: Locator) -> None:
        locator.wait_for(
            state="visible", 
            timeout=DEFAULT_TIMEOUT
        )

    def wait_for_hidden(self, locator: Locator) -> None:
        locator.wait_for(
            state="hidden",
            timeout=DEFAULT_TIMEOUT
        )

    def wait_for_url(self, url: str) -> None:
        self.page.wait_for_url(url, timeout=DEFAULT_TIMEOUT)

    def wait_for_timeout(self, milliseconds: int) -> None:
        self.page.wait_for_timeout(milliseconds)

    # -------------------------
    # Assertions
    # -------------------------
    def should_be_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible()

    def should_have_text(self, locator: Locator, text: str) -> None:
        expect(locator).to_have_text(text)

    def should_contain_text(self, locator: Locator, text: str) -> None:
        expect(locator).to_contain_text(text)

    def should_have_url(self, url: str) -> None:
        expect(self.page).to_have_url(url)
        
    def should_be_enabled(self, locator: Locator) -> None:
        expect(locator).to_be_enabled()

    def should_be_disabled(self, locator: Locator) -> None:
        expect(locator).to_be_disabled()

    # -------------------------
    # Utilities
    # -------------------------
    def screenshot(self, name: str) -> None:
        Path("reports/screenshots").mkdir(parents=True, exist_ok=True)
        self.page.screenshot(path=f"reports/screenshots/{name}.png")

    def get_by_test_id(self, test_id: str) -> Locator: 
        return self.page.get_by_test_id(test_id)