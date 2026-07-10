from playwright.sync_api import Page, expect

#LOCATORS FOR LOGIN PAGE

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        tid = page.get_by_test_id
        
        #LOGIN PAGE ELEMENTS
        self.email_input = tid("login-email-input")
        self.password_input = tid("login-password-input")
        self.login_button = tid("login-submit-button")
        self.forgot_password_link = tid("login-forgot-link")
        self.sign_up_link = tid("login-signup-link")
        self.error_message = tid("login-error")

        
        #ACTIONS FOR THE LOGIN PAGE
        
        #FILL EMAIL
    def fill_email(self, email: str):
        self.email_input.fill(email)
        
        #FILL PASSWORD
    def fill_password(self, password: str):
        self.password_input.fill(password)
        
        #CLICK LOGIN BUTTON
    def click_login(self):
        self.login_button.click()

        #LOGIN METHOD THAT COMBINES ALL ACTIONS
    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        
        #ERROR MESSAGE CHECK
    def wait_for_error_message(self):
        self.error_message.wait_for(state="visible")
        
    def get_error_message(self):
        return self.error_message.inner_text()
    