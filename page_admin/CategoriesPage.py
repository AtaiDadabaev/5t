from page_admin.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CategoriesPage(BasePage):
    link_main_page_categories = (By.LINK_TEXT, "Categories")
    tab_general = (By.LINK_TEXT, "General")
    tab_data = (By.LINK_TEXT, "Data")
    tab_seo = (By.LINK_TEXT, "SEO")
    tab_design = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[2]/div[1]/div[2]/form[1]/ul[1]/li[4]/a[1]")
    button_add_new_category = (By.CSS_SELECTOR, "a.btn.btn-primary:nth-child(2)")
    input_category_name = (By.CSS_SELECTOR, "#input-name-1")
    input_meta_tag_title = (By.CSS_SELECTOR, "#input-meta-title-1")
    input_meta_tag_description = (By.CSS_SELECTOR, "#input-meta-description-1")
    input_meta_tag_keywords = (By.CSS_SELECTOR, "#input-meta-keyword-1")
    button_save_category = (By.CSS_SELECTOR, "button.btn.btn-primary:nth-child(1)")
    select_parent = (By.CSS_SELECTOR, "#input-parent")
    option_parent_none = (By.PARTIAL_LINK_TEXT, "--- None -")
    input_filter = (By.CSS_SELECTOR, "#input-filter")
    input_columns = (By.CSS_SELECTOR, "#input-column")
    input_sort_order = (By.CSS_SELECTOR, "#input-sort-order")
    input_status = (By.CSS_SELECTOR, "#input-status")
    select_layout_override = (By.XPATH, "//tbody/tr[1]/td[2]/select[1]")
    input_keyword = (By.CSS_SELECTOR, "#input-keyword-0-1")

    def press_down_arrow(self):
        self.action.send_keys(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).perform()
        self.logger.info("Pressed 'Down Arrow'")
        return self

    def create_category(self, name: str, mtt: str, mtd: str, mtk: str, parent=None):
        self.click(self.button_add_new_category)

        self.input(self.input_category_name, name)
        self.input(self.input_meta_tag_title, mtt+name)
        self.input(self.input_meta_tag_description, mtd+name)
        self.input(self.input_meta_tag_keywords, mtk+name)

        self.click(self.tab_data)

        if parent is not None:
            self.input(self.select_parent, parent)
            self.click((By.LINK_TEXT, parent))
        else:
            self.click(self.select_parent)
            self.click(self.option_parent_none)

        self.click(self.tab_seo)
        self.input(self.input_keyword, name.lower()+"test")

        self.click(self.tab_design)
        self.click(self.select_layout_override)

        for _ in range(7):
            self.press_down_arrow()

        self.click(self.button_save_category)
        self.click(self.link_main_page_categories)
