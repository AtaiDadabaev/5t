from page_admin.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegPage(BasePage):
    INPUT_LOGIN = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    NEXT = (By.XPATH,
            "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/button[1]")

    def login(self):
        self.input(RegPage.INPUT_LOGIN, "user")
        self.input(RegPage.INPUT_PASSWORD, "bitnami")
        self.click(RegPage.NEXT)
