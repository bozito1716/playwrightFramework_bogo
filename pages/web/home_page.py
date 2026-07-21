from playwright.sync_api import Page
from pages.web.base_page import BasePage
from playwright.sync_api import expect

#---------- LOCATORS FOR THE HOME PAGE ELEMENTS ----------#

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
    

        # HEADER LINKS AND NAVIGATION BUTTONS
        self.how_it_works_link = self.get_by_test_id("nav-link-how-it-works")
        self.restaurants_link = self.get_by_test_id("nav-link-restaurants")
        self.membership_link = self.get_by_test_id("nav-link-membership")
        self.become_a_partner_link = self.get_by_test_id("nav-link-b2b")
        self.login_button = self.get_by_test_id("nav-login-link")
        self.start_trial_button = self.get_by_test_id("nav-start-trial-button")

        # HERO SECTION BUTTONS
        self.hero_start_trial_button = self.get_by_test_id("hero-start-trial-button")
        self.hero_how_it_works_button = self.get_by_test_id("hero-how-it-works-link")

        # ALL RESTAURANTS SECTION BUTTONS
        self.see_all_restaurants_button = self.get_by_test_id("restaurants-see-all-link")

        # PRICING SECTION BUTTONS
        self.start_trial_monthly_button = self.get_by_test_id("pricing-billing-monthly-button")
        self.start_trial_annual_button = self.get_by_test_id("pricing-billing-annual-button")
        self.pricing_start_trial_button = self.get_by_test_id("pricing-start-trial-button")

        # BECOME A PARTNER SECTION BUTTONS
        self.become_a_partner_button = self.get_by_test_id("become-a-partner-home")

        # APP STORE AND GOOGLE PLAY BUTTONS
        self.apple_store_button = self.get_by_test_id("final-cta-app-store-button")
        self.google_play_button = self.get_by_test_id("final-cta-google-play-button")

        # FOOTER LINKS
        self.footer_terms_link = self.get_by_test_id("footer-link-terms")
        self.footer_privacy_link = self.get_by_test_id("footer-link-privacy")
        self.footer_contact_us_link = self.get_by_test_id("footer-link-contact")
        self.footer_for_restaurants_link = self.get_by_test_id("footer-link-partners")
        
        
        #----------------------------#
        #ACTIONS/METHODS
        #---------------------------#

        #HOW IT WORKS LINK
    def open_how_it_works(self):
        self.should_be_visible(self.how_it_works_link)
        self.click(self.how_it_works_link)
        
        #RESTAURANTS LINK
    def open_restaurants(self):
        self.click(self.restaurants_link)
        
        #MEMBERSHIP LINK
    def open_membership(self):
        self.click(self.membership_link)

        #BECOME A PARTNER LINK
    def open_partner_page_from_header(self):
        self.click(self.become_a_partner_link)

        #LOGIN BUTTON
    def open_login(self):
        self.click(self.login_button)
        
        #START TRIAL BUTTON
    def open_trial_sign_up(self):
        self.click(self.start_trial_button)
    
        #HERO SECTION START TRIAL BUTTON
    def open_hero_start_trial(self):
        self.click(self.hero_start_trial_button)
        
        #SEE ALL RESTAURANTS BUTTON
    def open_see_all_restaurants(self):
        self.click(self.see_all_restaurants_button)
        
        #PRICING SECTION START TRIAL BUTTONS
    def open_start_trial_monthly(self):
        self.click(self.start_trial_monthly_button)
    def open_start_trial_annual(self):
        self.click(self.start_trial_annual_button)
    def open_pricing_start_trial(self):
        self.click(self.pricing_start_trial_button)
        
        #BECOME A PARTNER SECTION BUTTON
    def open_become_a_partner_from_hero_button(self):
        self.click(self.become_a_partner_button)
        
        #APP STORE AND GOOGLE PLAY BUTTONS
    def open_apple_store(self):
        self.click(self.apple_store_button)
    def open_google_play(self):
        self.click(self.google_play_button)
        
        #FOOTER LINKS
    def open_footer_terms(self):
        self.click(self.footer_terms_link)
    def open_footer_privacy(self):
        self.click(self.footer_privacy_link)
    def open_footer_contact_us(self):
        self.click(self.footer_contact_us_link)
    def open_footer_for_restaurants(self):
        self.click(self.footer_for_restaurants_link)
        
    def verify_header_navigation_is_visible(self) -> None:
        self.should_be_visible(self.how_it_works_link)
        self.should_be_visible(self.restaurants_link)
        self.should_be_visible(self.membership_link)
        self.should_be_visible(self.become_a_partner_link)
        
    def verify_login_and_trial_button_are_visible(self) -> None:
        self.should_be_visible(self.login_button)
        self.should_be_visible(self.start_trial_button)
        
    def verify_hero_section_is_visible(self) -> None:    
        self.should_be_visible(self.hero_start_trial_button)
        self.should_be_visible(self.hero_how_it_works_button)