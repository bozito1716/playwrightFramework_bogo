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
    
    login_page.wait_for_error_message()
    assert login_page.verify_error_message("Wrong email or password.")
