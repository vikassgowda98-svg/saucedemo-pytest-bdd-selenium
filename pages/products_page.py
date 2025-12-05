from selenium.webdriver.common.by import By
from base_page import BasePage


class ProductsPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "span.title")  # should be "Products"
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select.product_sort_container")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_title(self) -> str:
        return self.text_of(self.TITLE)

    def select_sort_option(self, value: str):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        select.select_by_value(value)

    def add_first_item_to_cart(self):
        first_btn = self.driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")[0]
        first_btn.click()

    def get_cart_count(self) -> int:
        return int(self.text_of(self.CART_BADGE))
