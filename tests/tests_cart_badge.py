import time
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@allure.title("Full E-commerce Flow with Cart Badge Check Before and After Removal + Shipping")
def test_full_flow_with_shipping(driver, products=["sauce-labs-backpack", "sauce-labs-bike-light"]):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    with allure.step("Login as standard_user"):
        login.login("standard_user", "secret_sauce")
        time.sleep(3)
        assert "inventory" in driver.current_url

    with allure.step("Add products to cart"):
        for product in products:
            inventory.add_product_by_id(product)
            time.sleep(1)  # wait for UI update
        time.sleep(2)

    actual_items_count = len(products)
    cart_badge_count_before = inventory.get_cart_count()
    print(f"Number of items selected: {actual_items_count}")
    print(f"Number shown in cart badge BEFORE removal: {cart_badge_count_before}")
    if cart_badge_count_before == actual_items_count:
        print("Cart badge verification BEFORE removal PASSED")
    else:
        print("Cart badge verification BEFORE removal FAILED")
    assert cart_badge_count_before == actual_items_count, "Cart badge does not match items selected"

    with allure.step("Go to cart and list products"):
        inventory.go_to_cart()
        time.sleep(3)
        cart_products = cart.get_all_products()
        print("Products in cart:", cart_products)

    with allure.step("Remove first product"):
        cart.remove_product_by_name(cart_products[0])
        time.sleep(3)
        remaining_products = cart.get_all_products()
        print("Products after removal:", remaining_products)

        cart_badge_count_after_removal = inventory.get_cart_count()
        print(f"Number of items remaining: {len(remaining_products)}")
        print(f"Number shown in cart badge AFTER removal: {cart_badge_count_after_removal}")
        if cart_badge_count_after_removal == len(remaining_products):
            print("Cart badge verification AFTER removal PASSED")
        else:
            print("Cart badge verification AFTER removal FAILED")
        assert cart_badge_count_after_removal == len(remaining_products), "Cart badge after removal mismatch"

    with allure.step("Checkout - enter shipping details"):
        cart.click_checkout()
        time.sleep(2)
        cart.enter_user_details(first_name="Aabhash", last_name="Shahi", postal_code="44600")
        cart.click_continue()
        time.sleep(2)

    with allure.step("Finish order"):
        cart.click_finish()
        time.sleep(3)
        assert "checkout-complete" in driver.current_url

    with allure.step("Logout"):
        inventory.logout()
        time.sleep(3)
        assert "saucedemo.com" in driver.current_url
