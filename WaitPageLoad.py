from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.expected_conditions import staleness_of


class waitPageLoad:
    def __init__(self, browser, message='', timeout=5):
        self.browser = browser
        self.message = message
        self.timeout = timeout
        
    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')
        self.old_title = self.browser.title
    
    def __exit__(self, *_):
        WebDriverWait(self.browser, self.timeout).until(staleness_of(self.old_page), self.message)