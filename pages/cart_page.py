from pages.base_page import BasePage


class CartPage(BasePage):

    PAGE_NAME = "cart_page"

    def get_title(self):
        return self.get_text(self.PAGE_NAME,"title")

    def get_cart_items(self):
        return self.get_elements(self.PAGE_NAME,"cart_items")

    def find_cart_item_names(self):
        return self.find_elements(self.PAGE_NAME,"cart_items")

    def click_checkout(self):
        self.click(self.PAGE_NAME,"checkout_button")

    def click_continue_shopping(self):
        self.click(self.PAGE_NAME,"continue_shopping")

    def remove_first_product(self):
        buttons = self.get_elements(self.PAGE_NAME,"remove_buttons")
        buttons[0].click()