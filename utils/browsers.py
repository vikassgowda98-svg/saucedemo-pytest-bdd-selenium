from selenium import webdriver


class DriverClass:

    @staticmethod
    def create_driver(browser, headless=False):

        browser = browser.lower()

        if browser == "chrome":

            options = webdriver.ChromeOptions()

            # Maximize browser
            options.add_argument("--start-maximized")

            # Disable browser notifications
            options.add_argument("--disable-notifications")

            # Disable password manager and password leak detection
            options.add_experimental_option(
                "prefs",
                {
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False,
                    "profile.password_manager_leak_detection": False
                }
            )

            # Headless mode
            if headless:
                options.add_argument("--headless")

            return webdriver.Chrome(options=options)

        elif browser == "edge":

            options = webdriver.EdgeOptions()

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            options.add_experimental_option(
                "prefs",
                {
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False,
                    "profile.password_manager_leak_detection": False
                }
            )

            if headless:
                options.add_argument("--headless")

            return webdriver.Edge(options=options)

        elif browser == "firefox":

            options = webdriver.FirefoxOptions()

            options.add_argument("--start-maximized")

            if headless:
                options.add_argument("--headless")

            return webdriver.Firefox(options=options)

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )