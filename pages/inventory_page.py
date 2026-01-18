from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    logout_menu = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    def add_product_by_id(self, product_id):
        btn = (By.ID, f"add-to-cart-{product_id}")
        self.driver.find_element(*btn).click()

    def remove_product_by_id(self, product_id):
        btn = (By.ID, f"remove-{product_id}")
        self.driver.find_element(*btn).click()

    def get_cart_count(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.cart_badge))
            return int(self.driver.find_element(*self.cart_badge).text)
        except:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def logout(self):
        self.driver.find_element(*self.logout_menu).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.logout_link)
        )
        self.driver.find_element(*self.logout_link).click()
