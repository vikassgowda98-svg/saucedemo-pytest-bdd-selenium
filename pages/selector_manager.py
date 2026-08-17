import json
from pathlib import Path

from selenium.webdriver.common.by import By


class SelectorManager:

    def __init__(self):

        selector_file = (Path(__file__).parent.parent/ "config"/ "selectors.json")
        
        with open(selector_file,"r",encoding="utf-8") as file:
            self.selectors = json.load(file)

    def get_selector(self,page_name,element_name):
        element = self.selectors[page_name][element_name]
        locator_map = {
            "id": By.ID,
            "name": By.NAME,
            "class name": By.CLASS_NAME,
            "css selector": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "tag name": By.TAG_NAME,
            "link text": By.LINK_TEXT,
            "partial link text": By.PARTIAL_LINK_TEXT
        }

        return (locator_map[element["by"]],element["value"])