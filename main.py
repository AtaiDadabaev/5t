import time
from conftest import *
from page_admin.AdminPage import AdminPage
from page_objects.MainPage import MainPage
from page_admin.ProductPage import ProductPage
from page_admin.RegPage import RegPage
from page_admin.AdminMainPage import AdminMainPage
from page_admin.CategoriesPage import CategoriesPage


@allure.feature("Create Categories")
@allure.title("Creating new categories 'Devices'")
def test_1(driver):
    RegPage(driver).login()
    AdminPage(driver).click(AdminPage.MENU_CATALOG)
    AdminPage(driver).click(AdminPage.LI_CATEGORIES)

    categories_page = CategoriesPage(driver)
    categories_page.create_category("Devices", "META_TAG_TITLE", "META_TAG_DESCRIPTION", "META_TAG_KEYWORDS")

    categories_page.create_category("mouse", "META_TAG_TITLE", "META_TAG_DESCRIPTION", "mousess", "Devices")
    categories_page.create_category("keyboard", "META_TAG_TITLE", "META_TAG_DESCRIPTION", "keyboardd", "Devices")


@allure.feature("Add products")
@allure.title("Creating 4 new products in 'Devices'")
def test_2(driver):
    RegPage(driver).login()
    AdminMainPage(driver).click(AdminMainPage.MENU_CATALOG)
    AdminMainPage(driver).click(AdminMainPage.LI_PRODUCTS)

    ProductPage(driver).add_product([
        ["Mouse", "model_mouse", "1"],
        ["Keyboard", "keyboard_model", "0"],
        ["Mouse2", "model_mouse", "1"],
        ["Keyboard2", "keyboard_model", "0"],
    ])


@allure.feature("Checking products")
@allure.title("Checking all products in main page")
def test_3(driver):
    driver.get("http:/localhost")
    MainPage(driver).input(MainPage.search, "mouse")
    MainPage(driver).enter()
    MainPage(driver).input(MainPage.search, "keyboard")
    MainPage(driver).enter()


@allure.feature("Delete products")
@allure.title("Deleting 2 products")
def test_4(driver):
    RegPage(driver).login()
    AdminMainPage(driver).click(AdminMainPage.MENU_CATALOG)
    AdminMainPage(driver).click(AdminMainPage.LI_PRODUCTS)

    ProductPage(driver).delete_product(["Mouse", "model_mouse", "1"])
    ProductPage(driver).delete_product(["Keyboard", "keyboard_model", "0"])
    time.sleep(2)


@allure.feature("Checking products")
@allure.title("Checking all products in main page")
def test_5(driver):
    driver.get("http:/localhost")
    MainPage(driver).input(MainPage.search, "mouse")
    MainPage(driver).enter()
    MainPage(driver).input(MainPage.search, "keyboard")
    MainPage(driver).enter()
