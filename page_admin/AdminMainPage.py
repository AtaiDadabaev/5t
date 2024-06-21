from page_admin.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminMainPage(BasePage):
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    LI_CATEGORIES = (By.LINK_TEXT, "Categories")
    LI_PRODUCTS = (By.LINK_TEXT, "Products")