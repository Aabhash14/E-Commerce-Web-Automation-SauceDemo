import time
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.performance_test import measure_page_load, measure_action_time, measure_full_flow_times


@allure.title("Full E-commerce Flow with Cart Badge Check and Shipping")
def test_full_flow_with_shipping(driver, products=["sauce-labs-backpack", "sauce-labs-bike-light"]):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    with allure.step("Load SauceDemo home page"):
        measure_page_load(driver, "https://www.saucedemo.com/")

    with allure.step("Login as standard_user"):
        measure_action_time(login.login, "standard_user", "secret_sauce")
        time.sleep(3)
        assert "inventory" in driver.current_url

    with allure.step("Add products to cart"):
        for product in products:
            measure_action_time(inventory.add_product_by_id, product)
            time.sleep(1)
        time.sleep(2)

    actual_items_count = len(products)
    cart_badge_count = inventory.get_cart_count()
    print(f"Number of items added: {actual_items_count}")
    print(f"Number shown in cart badge: {cart_badge_count}")
    if cart_badge_count == actual_items_count:
        print("Cart badge verification PASSED")
    else:
        print("Cart badge verification FAILED")
    assert cart_badge_count == actual_items_count, "Cart badge does not match number of items added"

    with allure.step("Go to cart and list products"):
        measure_action_time(inventory.go_to_cart)
        time.sleep(3)
        cart_products = cart.get_all_products()
        print("Products in cart:", cart_products)

    with allure.step("Remove first product"):
        measure_action_time(cart.remove_product_by_name, cart_products[0])
        time.sleep(3)
        remaining_products = cart.get_all_products()
        print("Products after removal:", remaining_products)

        # Verify cart badge again after removal
        cart_badge_count_after_removal = inventory.get_cart_count()
        print(f"Number of items remaining: {len(remaining_products)}")
        print(f"Number shown in cart badge after removal: {cart_badge_count_after_removal}")
        if cart_badge_count_after_removal == len(remaining_products):
            print("Cart badge after removal PASSED")
        else:
            print("Cart badge after removal FAILED")
        assert cart_badge_count_after_removal == len(remaining_products), "Cart badge after removal mismatch"

    with allure.step("Checkout - enter shipping details"):
        cart.click_checkout()
        time.sleep(2)
        measure_action_time(cart.enter_user_details, "Aabhash", "Shahi", "44600")
        measure_action_time(cart.click_continue)
        time.sleep(2)

    with allure.step("Finish order"):
        measure_action_time(cart.click_finish)
        time.sleep(3)
        assert "checkout-complete" in driver.current_url

    with allure.step("Logout"):
        measure_action_time(inventory.logout)
        time.sleep(3)
        assert "saucedemo.com" in driver.current_url
