from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.selector_manager import SelectorManager


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.selector_manager = (SelectorManager())

    def open(self, url):
        self.driver.get(url)

    def get_element(self,page_name,element_name):
        locator = (self.selector_manager.get_selector(page_name,element_name))
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_elements(self,page_name,element_name):
        locator = (self.selector_manager.get_selector(page_name,element_name))
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self,page_name,element_name):
        element = self.get_element(page_name,element_name)
        element.click()

    def type_text(self,age_name,element_name,text):
        element = self.get_element(page_name,element_name)
        element.clear()
        element.send_keys(text)

    def get_text(self,page_name,element_name):
        return self.get_element(page_name,element_name).text

    def is_displayed(self,page_name,element_name):
        try:
            return self.get_element(page_name,element_name).is_displayed()
        except Exception:
            return False