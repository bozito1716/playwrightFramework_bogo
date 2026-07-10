from playwright.sync_api import Page

#---------- LOCATORS FOR THE HOME PAGE ELEMENTS ----------#

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        tid = page.get_by_test_id

        # HEADER LINKS AND NAVIGATION BUTTONS
        self.how_it_works_link = tid("nav-link-how-it-works")
        self.restaurants_link = tid("nav-link-restaurants")
        self.membership_link = tid("nav-link-membership")
        self.become_a_partner_link = tid("nav-link-b2b")
        self.login_button = tid("nav-login-link")
        self.start_trial_button = tid("nav-start-trial-button")

        # HERO SECTION BUTTONS
        self.hero_start_trial_button = tid("hero-start-trial-button")

        # ALL RESTAURANTS SECTION BUTTONS
        self.see_all_restaurants_button = tid("restaurants-see-all-link")

        # PRICING SECTION BUTTONS
        self.start_trial_monthly_button = tid("pricing-billing-monthly-button")
        self.start_trial_annual_button = tid("pricing-billing-annual-button")
        self.pricing_start_trial_button = tid("pricing-start-trial-button")

        # BECOME A PARTNER SECTION BUTTONS
        self.become_a_partner_button = tid("biz-teaser-cta-link")

        # APP STORE AND GOOGLE PLAY BUTTONS
        self.apple_store_button = tid("final-cta-app-store-button")
        self.google_play_button = tid("final-cta-google-play-button")

        # FOOTER LINKS
        self.footer_terms_link = tid("footer-link-terms")
        self.footer_privacy_link = tid("footer-link-privacy")
        self.footer_contact_us_link = tid("footer-link-contact")
        self.footer_for_restaurants_link = tid("footer-link-partners")

        #HOW IT WORKS LINK
    def open_how_it_works(self):
        self.how_it_works_link.click()
        
        #RESTAURANTS LINK
    def open_restaurants(self):
        self.restaurants_link.click()
        
        #MEMBERSHIP LINK
    def open_membership(self):
        self.membership_link.click()

        #BECOME A PARTNER LINK
    def open_partner_page_from_header(self):
        self.become_a_partner_link.click()

        #LOGIN BUTTON
    def open_login(self):
        self.login_button.click()
        
        #START TRIAL BUTTON
    def open_trial_sign_up(self):
        self.start_trial_button.click()
    
        #HERO SECTION START TRIAL BUTTON
    def open_hero_start_trial(self):
        self.hero_start_trial_button.click()
        
        #SEE ALL RESTAURANTS BUTTON
    def open_see_all_restaurants(self):
        self.see_all_restaurants_button.click()
        
        #PRICING SECTION START TRIAL BUTTONS
    def open_start_trial_monthly(self):
        self.start_trial_monthly_button.click()
    def open_start_trial_annual(self):
        self.start_trial_annual_button.click()
    def open_pricing_start_trial(self):
        self.pricing_start_trial_button.click()
        
        #BECOME A PARTNER SECTION BUTTON
    def open_become_a_partner_from_hero_button(self):
        self.become_a_partner_button.click()
        
        #APP STORE AND GOOGLE PLAY BUTTONS
    def open_apple_store(self):
        self.apple_store_button.click()
    def open_google_play(self):
        self.google_play_button.click()
        
        #FOOTER LINKS
    def open_footer_terms(self):
        self.footer_terms_link.click()
    def open_footer_privacy(self):
        self.footer_privacy_link.click()
    def open_footer_contact_us(self):
        self.footer_contact_us_link.click()
    def open_footer_for_restaurants(self):
        self.footer_for_restaurants_link.click()
        
        



           
           
           