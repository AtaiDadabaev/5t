from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, wait=10):
        self.driver = driver
        self.logger = driver.logger
        self.wait = WebDriverWait(self.driver, wait)
        self.action = ActionChains(self.driver)
        self.class_name = self.__class__.__name__

    def left(self):
        self.action.send_keys(Keys.CONTROL).send_keys(Keys.ARROW_LEFT).perform()
        return self

    def enter(self):
        self.action.send_keys(Keys.CONTROL).send_keys(Keys.ENTER).perform()
        return self

    def element_name(self, element_locator):
        try:
            element = self.find_element(element_locator)
            return self._get_element_name(element_locator, element)
        except Exception as e:
            self.logger.error(f"Error getting element name: {e}")
            return str(element_locator)

    def _get_element_name(self, element_locator, element):
        for name, value in vars(self.__class__).items():
            if isinstance(value, (list, tuple)) and element_locator in value:
                return f"{name}[{value.index(element_locator)}]"
            elif value == element_locator:
                return name
        return str(element_locator)

    def find_element(self, element_locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(element_locator))
            return element
        except Exception as e:
            self.logger.error(f"Error finding element: {e}")
            return None

    def click(self, element_locator):
        try:
            element = self.find_element(element_locator)
            if element is None:
                raise Exception("Element not found")
            element_name = self.element_name(element_locator)
            self.wait.until(EC.element_to_be_clickable(element_locator)).click()
            self.logger.info(f"{self.class_name}: Clicked |{element_name}|")
        except Exception as e:
            self.logger.error(f"Error clicking element: {e}")

        return self

    def input(self, element_locator, value):
        try:
            element = self.find_element(element_locator)
            if element is None:
                raise Exception("Element not found")
            self.click(element_locator)
            self.wait.until(EC.visibility_of(element))
            element.clear()
            element.send_keys(value)
            self.logger.info(f"{self.class_name}: Writing |{value}| to |{self.element_name(element_locator)}|")
            self.wait.until(EC.text_to_be_present_in_element_value(element_locator, value))
        except Exception as e:
            self.logger.error(f"Error inputting to element: {e}")

        return self
