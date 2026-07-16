import os

from dotenv import load_dotenv
from pages.web.login_page import LoginPage
from utils.test_data import LoginData
load_dotenv()


#SUCCESSFUL LOGIN TEST CASE
def test_successful_login(login_page: LoginPage):
    
    login_page.login(

        os.environ["VALID_EMAIL"],
        os.environ["VALID_PASSWORD"]

    )
    
    login_page.wait_for_url("**/restaurants")
    assert "/restaurants" in login_page.get_current_url()
    
#UNSUCCESSFUL LOGIN TEST CASE   
def test_unsuccessful_login(login_page: LoginPage):
    
    login_page.login(

        LoginData.INVALID_EMAIL,
        LoginData.INVALID_PASSWORD

    )
    
    login_page.verify_error_message("Wrong email or password.")
    
    
#TEST LOGIN BUTTON IS DISABLED
def test_login_button_disabled_with_invalid_email(login_page: LoginPage):
    
    login_page.fill_email(LoginData.INVALID_EMAIL_FORMAT)
    login_page.fill_password(LoginData.INVALID_PASSWORD)
    
    login_page.verify_login_button_disabled()

def test_login_button_disabled_when_fields_are_empty(login_page: LoginPage):
    
    login_page.verify_login_button_disabled()
    
def test_login_button_disabled_when_email_field_is_empty(login_page: LoginPage):
    
    login_page.fill_password(LoginData.VALID_PASSWORD_FORMAT)
    login_page.verify_login_button_disabled()

#TEST LOGIN BUTTON IS ENABLE
def test_login_button_enable_with_valid_email(login_page: LoginPage):
    
    login_page.fill_email(LoginData.VALID_EMAIL_FORMAT)
    login_page.fill_password(LoginData.VALID_PASSWORD_FORMAT)
    
    login_page.verify_login_button_enabled
    
def test_login_button_enable_with_one_char_password(login_page: LoginPage):
    
    login_page.fill_email(LoginData.VALID_EMAIL_FORMAT)
    login_page.fill_password("a")
    
    login_page.verify_login_button_enabled
    

