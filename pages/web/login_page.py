from playwright.sync_api import Page
from pages.web.base_page import BasePage

#LOCATORS FOR LOGIN PAGE

class LoginPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        
        #LOGIN PAGE ELEMENTS
        self.email_input = self.get_by_test_id("login-email-input")
        self.password_input = self.get_by_test_id("login-password-input")
        self.login_button = self.get_by_test_id("login-submit-button")
        self.forgot_password_link = self.get_by_test_id("login-forgot-link")
        self.create_account_link = self.get_by_test_id("login-signup-link")
        
        self.error_message = self.get_by_test_id("login-error")

        
        # ----------------------------------
        # Login Actions
        # ----------------------------------
        
        #FILL EMAIL
    def fill_email(self, email: str) -> None:
        self.fill(self.email_input, email)
        
        #FILL PASSWORD
    def fill_password(self, password: str) -> None:
        self.fill(self.password_input, password)
        
        #CLICK LOGIN BUTTON
    def click_login(self) -> None:
        self.click(self.login_button)
        
    def click_forgot_password_link(self) -> None:
        self.click(self.forgot_password_link)
    
    def click_create_account_button(self) -> None:
        self.click(self.create_account_link)
        
    #LOGIN METHOD THAT COMBINES ALL ACTIONS
    def login(self, email: str, password: str) -> None:
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()
        
   
    # -------------------------
    # Verifications/Assertions
    # -------------------------

    def verify_error_message(self, message: str) -> None:
        self.wait_for_visible(self.error_message)
        self.should_have_text(self.error_message, message)
        
    def verify_login_button_enabled(self) -> None:
        self.should_be_enabled(self.login_button)
        
    def verify_login_button_disabled(self) -> None:
        self.should_be_disabled(self.login_button)
    
    def should_be_loaded(self) -> None:
        self.should_be_visible(self.email_input)
        self.should_be_visible(self.password_input)
        self.should_be_visible(self.login_button)