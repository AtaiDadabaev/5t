import time
from page_admin.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint


class ProductPage(BasePage):
    tab_data = (By.LINK_TEXT, "Data")
    tab_seo = (By.LINK_TEXT, "SEO")
    tab_links = (By.LINK_TEXT, "Links")
    tab_general = (By.LINK_TEXT, "General")
    link_main_page_product = (By.LINK_TEXT, "Products")
    button_filter = (By.CSS_SELECTOR, "#button-filter")
    input_product_name_filter = (By.CSS_SELECTOR, "#input-name")
    checkbox_first_product = (By.XPATH, "//tbody/tr[1]/td[1]/input[1]")
    button_delete = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/button[3]")
    button_add_new_product = (By.CSS_SELECTOR, "a.btn.btn-primary:nth-child(2)")
    input_product_name = (By.CSS_SELECTOR, "#input-name-1")
    input_meta_tag_title = (By.CSS_SELECTOR, "#input-meta-title-1")
    input_meta_tag_description = (By.CSS_SELECTOR, "#input-meta-description-1")
    input_meta_tag_keywords = (By.CSS_SELECTOR, "#input-meta-keyword-1")
    button_save_product = (By.CSS_SELECTOR, "button.btn.btn-primary:nth-child(1)")
    input_model = (By.CSS_SELECTOR, "#input-model")
    input_keyword = (By.CSS_SELECTOR, "#input-keyword-0-1")
    input_choice_categories = (By.CSS_SELECTOR, "#input-category")
    select_devices = (By.XPATH, "//a[contains(text(),'Devices')]")

    def press_tab(self):
        self.action.send_keys(Keys.TAB).perform()
        self.logger.info("Pressed 'TAB'")

    def press_enter(self):
        self.action.send_keys(Keys.ENTER).perform()
        self.logger.info("Pressed 'ENTER'")

    def add_product(self, products):
        for product in products:
            name = product[0]
            model = product[1]
            full_name = f"{name} {model}"

            self.click(self.button_add_new_product)
            self.input(self.input_product_name, full_name)
            self.input(self.input_meta_tag_title, name)
            self.click(self.tab_data)
            self.input(self.input_model, model)
            self.click(self.tab_links)

            category = "mouse" if product[2] == "1" else "keyboard" if product[2] == "0" else "Devices"
            self.input(self.input_choice_categories, category)

            time.sleep(0.5)
            self.press_tab()
            self.press_enter()
            self.click(self.tab_seo)

            keyword = "".join(name.replace(" ", "")[randint(0, len(name) - 1)] for _ in range(len(name)))
            self.input(self.input_keyword, keyword)
            self.click(self.button_save_product)
            self.click(self.link_main_page_product)

    def filter_products(self, products):
        for product in products:
            name = product[0]
            model = product[1]

            self.click(self.link_main_page_product)
            self.input(self.input_product_name_filter, name)
            self.input(self.input_model, model)
            self.click(self.button_filter)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def find_product_by_name_and_model(self, name, model):
        self.click(self.link_main_page_product)
        self.input(self.input_product_name_filter, name)
        self.input(self.input_model, model)
        self.click(self.button_filter)

    def delete_product(self, product):
        self.find_product_by_name_and_model(product[0], product[1])
        self.click(self.checkbox_first_product)
        self.click(self.button_delete)
        self.accept_alert()
