from playwright.sync_api import Page
from pages.web.base_page import BasePage

#----------------#
# LOCATORS FOR THE SIGN UP ELEMENTS 
# --------------#

class SignUpPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.name_input = self.get_by_test_id("join-name-input")
        self.email_input = self.get_by_test_id("join-email-input")
        self.password_input = self.get_by_test_id("join-password-input")
        self.create_account_button = self.get_by_test_id("join-submit-button")
        self.login_link = self.get_by_test_id("join-login-link")
        
#----------------#
# ACTIONS FOR THE SIGN UP ELEMENTS 
# ----------------#  
    def fill_name(self, name: str) -> None:
        self.fill(self.name_input, name)
             
    def fill_email(self, email: str) -> None:
        self.fill(self.email_input, email)
        
    def fill_password(self, password: str) -> None:
        self.fill(self.password_input, password)
        
    def click_create_account_button(self) -> None:
        self.click(self.create_account_button)
    
    def click_login_link(self) -> None:
        self.click(self.login_link)
    
    #SignUp Method
    def sign_up(self, name: str, email: str, password: str):
        self.fill_name(name)
        self.fill_email(email)
        self.fill_password(password)
        self.click_create_account_button()
        