import re #for regular expresions
from playwright.sync_api import Page, expect #for verification 

def test_home_page(page: Page):
    page.wait_for_timeout(3000) #wait for 3 second
    
    page.goto("https://www.bogogourmet.com/") #Open Bogo page
    
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000) #click the accept cookies button
    except:
        print("No cookies button found")
    

    expect(page).to_have_title(re.compile("Bogo Gourmet", re.IGNORECASE)) #verify the page title