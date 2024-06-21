from selenium.webdriver.common.by import By
from page_admin.BasePage import BasePage


class MainPage(BasePage):
    search = (By.CSS_SELECTOR, "input.form-control.form-control-lg")
