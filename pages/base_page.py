from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

from pages.selector_manager import SelectorManager


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.selector_manager = (SelectorManager())

    def open(self, url):
        self.driver.get(url)

    def get_element(self,page_name,element_name):
        try:
            locator = (self.selector_manager.get_selector(page_name,element_name))
            return self.wait.until(EC.visibility_of_element_located(locator))
        except (TimeoutException, StaleElementReferenceException) as e:
            print(f"Element lookup failed: {locator}")
            print("Refreshing page and retrying...")
            self.driver.refresh()
            try:
                locator = (self.selector_manager.get_selector(page_name,element_name))
                return self.wait.until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                print(f"Element still not found after refresh: {locator}")
                raise e

    def get_elements(self,page_name,element_name):
        try:
            locator = (self.selector_manager.get_selector(page_name,element_name))
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except (TimeoutException, StaleElementReferenceException) as e:
            print(f"Elements lookup failed: {locator}")
            print("Refreshing page and retrying...")
            self.driver.refresh() 
            try:
                locator = (self.selector_manager.get_selector(page_name,element_name))
                return self.wait.until(EC.presence_of_all_elements_located(locator))
            except TimeoutException:
                print(f"Elements still not found after refresh: {locator}")
                raise e
    
    def find_elements(self,page_name,element_name):
        try:
            locator = (self.selector_manager.get_selector(page_name,element_name))
            return self.driver.find_elements(*locator)
        except (TimeoutException, StaleElementReferenceException) as e:
            print(f"Finding elements failed: {locator}")
            print("Refreshing page and retrying...")
            self.driver.refresh() 
            try:
                locator = (self.selector_manager.get_selector(page_name,element_name))
                return self.driver.find_elements(*locator)
            except (TimeoutException, StaleElementReferenceException):
                print(f"Elements still not found after refresh: {locator}")
                raise e

    def click(self,page_name,element_name):
        try:
            element = self.get_element(page_name,element_name)
            element.click()
        except (TimeoutException, StaleElementReferenceException) as e:
            print(f"Click failed on element {element_name}")
            print("Refreshing page and retrying...")           
            self.driver.refresh()           
            try:
                element = self.get_element(page_name,element_name)
                element.click()
            except (TimeoutException, StaleElementReferenceException):
                print(f"Click still failed after refresh on element {element_name}")
                raise e

    def type_text(self, page_name, element_name, text):
        try:
            element = self.get_element(page_name, element_name)
            element.clear()
            element.send_keys(text)
        except (TimeoutException, StaleElementReferenceException) as e:
            print(f"Type text failed on element {element_name}")
            print("Refreshing page and retrying...")
            
            self.driver.refresh()
            
            try:
                element = self.get_element(page_name, element_name)
                element.clear()
                element.send_keys(text)
            except (TimeoutException, StaleElementReferenceException):
                print(f"Type text still failed after refresh on element {element_name}")
                raise e

    def get_text(self,page_name,element_name):
        try:
            return self.get_element(page_name,element_name).text
        except (TimeoutException, StaleElementReferenceException) as e:
            print(f"Get text failed on element {element_name}")
            print("Refreshing page and retrying...")
            
            self.driver.refresh()
            
            try:
                return self.get_element(page_name,element_name).text
            except (TimeoutException, StaleElementReferenceException):
                print(f"Get text still failed after refresh on element {element_name}")
                raise e

    def is_displayed(self,page_name,element_name):
        try:
            return self.get_element(page_name,element_name).is_displayed()
        except Exception:
            return False