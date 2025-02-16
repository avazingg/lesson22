class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.goto(url)

    def find_element(self, selector, timeout=10000):
        try:
            return self.driver.wait_for_selector(selector, timeout=timeout)
        except Exception:
            return None

    def click_element(self, selector, timeout=10000):
        element = self.find_element(selector, timeout)
        if element:
            element.click()

    def enter_text(self, selector, text, timeout=10000):
        element = self.find_element(selector, timeout)
        element.fill(text)