from pages.web.home_page import HomePage
from pages.web.login_page import LoginPage
from pages.web.sign_up_page import SignUpPage


def test_header_navigation_is_displayed(home_page: HomePage):
    home_page.verify_header_navigation_is_visible()
    
def test_login_and_trial_button_are_displayed(home_page: HomePage):
    home_page.verify_login_and_trial_button_are_visible()
    
def test_hero_section_is_visible(home_page: HomePage):
    home_page.verify_hero_section_is_visible()
    
def test_user_can_navigate_to_login_page(home_page: HomePage,login_page: LoginPage):
    home_page.open_login()
    login_page.should_have_url("/login")
    
def test_user_can_navigate_to_the_sign_up_page(home_page: HomePage, sign_up_page: SignUpPage):
    home_page.open_trial_sign_up()
    sign_up_page.should_have_url("/join")
    
def test_user_can_navigate_to_how_it_works_page(home_page: HomePage):
    home_page.open_how_it_works()
    home_page.should_have_url("/how-it-works")
    
def test_user_can_navigate_to_restaurants_page(home_page: HomePage):
    home_page.open_restaurants()
    home_page.should_have_url("/restaurants")
    
def test_user_can_navigate_to_membership_page(home_page: HomePage):
    home_page.open_membership()
    home_page.should_have_url("/membership")

def test_user_can_navigate_to_become_a_partner_page(home_page: HomePage):
    home_page.open_partner_page_from_header()
    home_page.should_have_url("/for-restaurants")

def test_user_can_navigate_to_signup_page_from_hero_button(home_page: HomePage):
    home_page.open_hero_start_trial()
    home_page.should_have_url("/join")

def test_user_can_navigate_to_all_restaurants_page_from_link(home_page: HomePage):
    home_page.open_see_all_restaurants()
    home_page.should_have_url("/restaurants")

def test_user_can_navigate_to_join_page_with_monthly_pricing(home_page: HomePage):
    home_page.open_start_trial_monthly()
    home_page.open_pricing_start_trial()
    home_page.should_have_url("/join?plan=monthly")
    
def test_user_can_navigate_to_join_page_with_annual_pricing(home_page: HomePage):
    home_page.open_start_trial_annual()
    home_page.open_pricing_start_trial()
    home_page.should_have_url("/join?plan=annual")
    
def test_user_can_navigate_to_become_a_parter_page_from_hero_button(home_page: HomePage):
    home_page.open_become_a_partner_from_hero_button()
    home_page.should_have_url("/for-restaurants")

