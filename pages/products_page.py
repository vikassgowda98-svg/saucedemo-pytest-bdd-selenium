from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class ProductsPage(BasePage):

    PAGE_NAME = "products_page"

    def get_title(self):
        return self.get_text(self.PAGE_NAME,"title")

    def get_product_items(self):
        return self.get_elements(self.PAGE_NAME,"inventory_items")

    def get_product_names(self):
        return self.get_elements(self.PAGE_NAME,"product_names")

    def get_product_prices(self):
        return self.get_elements(self.PAGE_NAME,"product_prices")

    def get_add_to_cart_buttons(self):
        return self.get_elements(self.PAGE_NAME,"add_to_cart_buttons")

    def add_first_product_to_cart(self):
        buttons = (self.get_add_to_cart_buttons())
        buttons[0].click()

    def add_product_by_index(self,index):
        buttons = (self.get_add_to_cart_buttons())
        buttons[index].click()

    def get_cart_count(self):
        return self.get_text(self.PAGE_NAME,"cart_badge")

    def open_cart(self):
        self.click(self.PAGE_NAME,"cart_icon")

    def sort_products(self,value):
        dropdown = self.get_element(self.PAGE_NAME,"sort_dropdown")
        Select(dropdown).select_by_value(value)

    def open_menu(self):
        self.click(self.PAGE_NAME,"menu_button")

    def logout(self):
        self.click(self.PAGE_NAME,"logout_link")