import os
import pytest
from dotenv import load_dotenv
from pages.web.login_page import LoginPage
from utils.test_data import LoginData
load_dotenv()


class TestLogin:
    """
    Login page test suite.

    Smoke:
        Critical login flows required after deployment.

    Regression:
        Complete login behavior validation.
    """
    
    #PAGE SHOULD LOAD
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_page_is_loaded(self, login_page: LoginPage):
        login_page.should_be_loaded()

    #SUCCESSFUL LOGIN TEST CASE
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_user_can_login_with_valid_credentials(self, login_page: LoginPage):
        
        login_page.login(

            os.environ["VALID_EMAIL"],
            os.environ["VALID_PASSWORD"]
        )
        login_page.wait_for_url("**/restaurants")
        assert "/restaurants" in login_page.get_current_url()
    
    
  
    #UNSUCCESSFUL LOGIN TEST CASE
    @pytest.mark.regression
    def test_user_cannot_login_with_invalid_credentials(self, login_page: LoginPage):
        
        login_page.login(

            LoginData.INVALID_EMAIL,
            LoginData.INVALID_PASSWORD

        )
        
        login_page.verify_error_message("Wrong email or password.")
        
        
    #TEST LOGIN BUTTON IS DISABLED
    @pytest.mark.regression
    def test_login_button_disabled_with_invalid_email(self, login_page: LoginPage):
        
        login_page.fill_email(LoginData.INVALID_EMAIL_FORMAT)
        login_page.fill_password(LoginData.INVALID_PASSWORD)
        login_page.verify_login_button_disabled()

    @pytest.mark.regression
    def test_login_button_disabled_when_fields_are_empty(self, login_page: LoginPage):
        login_page.verify_login_button_disabled()

    @pytest.mark.regression  
    def test_login_button_disabled_when_email_field_is_empty(self, login_page: LoginPage):
        
        login_page.fill_password(LoginData.VALID_PASSWORD_FORMAT)
        login_page.verify_login_button_disabled()
        
    @pytest.mark.regression    
    def test_login_button_disabled_when_password_field_is_empty(self, login_page: LoginPage):
        
        login_page.fill_email(LoginData.VALID_EMAIL_FORMAT)
        login_page.verify_login_button_disabled()
        
    #TEST LOGIN BUTTON IS ENABLE
    @pytest.mark.regression
    def test_login_button_enable_with_valid_email(self, login_page: LoginPage):
        
        login_page.fill_email(LoginData.VALID_EMAIL_FORMAT)
        login_page.fill_password(LoginData.VALID_PASSWORD_FORMAT)
        login_page.verify_login_button_enabled()
        
    @pytest.mark.regression    
    def test_login_button_enable_with_one_char_password(self, login_page: LoginPage):
        
        login_page.fill_email(LoginData.VALID_EMAIL_FORMAT)
        login_page.fill_password("a")
        login_page.verify_login_button_enabled()
        
    #TEST USER STAYS LOGGED IN AFTER REFRESH
    @pytest.mark.regression
    def test_user_stays_logged_in_after_page_refresh(self, login_page: LoginPage):
        login_page.login(

            os.environ["VALID_EMAIL"],
            os.environ["VALID_PASSWORD"]
        )
        login_page.wait_for_url("**/restaurants")
        login_page.refresh()
        login_page.wait_for_url("**/restaurants")
        assert "/restaurants" in login_page.get_current_url()
        
    #TEST LOGIN IN USING ENTER KEY
    @pytest.mark.regression
    def test_user_can_login_using_enter_key(self, login_page: LoginPage):
        
        login_page.fill_email(os.environ["VALID_EMAIL"])
        login_page.fill_password(os.environ["VALID_PASSWORD"])
        login_page.press(login_page.password_input, "Enter")
        login_page.wait_for_url("**/restaurants")

        assert "/restaurants" in login_page.get_current_url()

    #IMPLEMENT A TEST ABOUT GOING TO LOGIN WHEN LOGGED IN

    #FORGOT PASSWORD NAVIGATION
    @pytest.mark.regression
    def test_user_can_open_forgot_password_page(self, login_page: LoginPage):
        login_page.click_forgot_password_link()
        login_page.should_have_url("/forgot-password")
        
    #CREATE AN ACCOUNT LINK
    @pytest.mark.regression
    def test_user_can_open_join_page(self, login_page: LoginPage):
        login_page.click_create_account_button()
        login_page.should_have_url("/join")
        