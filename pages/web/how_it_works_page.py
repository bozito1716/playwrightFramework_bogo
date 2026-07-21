from playwright.sync_api import Page
from pages.web.base_page import BasePage

#----------------#
# LOCATORS FOR THE HOW IT WORKS PAGE ELEMENTS 
# --------------#

class HowItWorksPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.apple_store_download_button=self.get_by_test_id("hiw-hero-app-store-button")
        self.google_play_download_button=self.get_by_test_id("hiw-hero-google-play-button")
        self.hero_trial_button=self.get_by_test_id("hiw-hero-trial-link")
        self.trial_start_button=self.get_by_test_id("hiw-plan-start-trial-button")
        self.bottom_apple_store_download_button=self.get_by_test_id("final-cta-app-store-button")
        self.bottom_google_play_download_button=self.get_by_test_id("final-cta-google-play-button")
        
        
#----------------#
# ACTIONS/METHODS FOR THE HOW IT WORKS PAGE ELEMENTS 
# --------------#
        
    def open_apple_store(self) -> None:
        self.click(self.apple_store_download_button)
        
    def open_google_play(self) -> None:
        self.click(self.apple_store_download_button)
    
    def open_join_from_hero_button_on_how_it_works(self) -> None:
        self.click(self.hero_trial_button)
    
    def open_join_from_start_trial_button_on_how_it_works(self) -> None:
        self.click(self.trial_start_button)
        
    def open_apple_store_from_bottom_page(self) -> None:
        self.click(self.bottom_apple_store_download_button)
        
    def open_google_play_from_bottom_page(self) -> None:
        self.click(self.bottom_google_play_download_button)