from page_admin.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")

    # CATEGORIES
    LI_CATEGORIES = (By.LINK_TEXT, "Categories")

    # Products
    LI_PRODUCTS = (By.LINK_TEXT, "Products")