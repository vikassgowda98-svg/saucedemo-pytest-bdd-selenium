from pages.base_page import BasePage


class CheckoutPage(BasePage):

    PAGE_NAME = "checkout_page"

    def enter_first_name(
        self,
        first_name
    ):

        self.type_text(
            self.PAGE_NAME,
            "first_name",
            first_name
        )

    def enter_last_name(
        self,
        last_name
    ):

        self.type_text(
            self.PAGE_NAME,
            "last_name",
            last_name
        )

    def enter_postal_code(
        self,
        postal_code
    ):

        self.type_text(
            self.PAGE_NAME,
            "postal_code",
            postal_code
        )

    def click_continue(self):

        self.click(
            self.PAGE_NAME,
            "continue_button"
        )

    def click_cancel(self):

        self.click(
            self.PAGE_NAME,
            "cancel_button"
        )

    def click_finish(self):

        self.click(
            self.PAGE_NAME,
            "finish_button"
        )

    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.enter_first_name(
            first_name
        )

        self.enter_last_name(
            last_name
        )

        self.enter_postal_code(
            postal_code
        )

    def get_error_message(self):

        return self.get_text(
            self.PAGE_NAME,
            "error_message"
        )

    def get_confirmation_message(
        self
    ):

        return self.get_text(
            self.PAGE_NAME,
            "confirmation_message"
        )