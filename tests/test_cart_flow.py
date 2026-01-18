# from pages.login_page import LoginPage
# from pages.inventory_page import InventoryPage
# from pages.cart_page import CartPage
# import pytest, time

# @pytest.mark.parametrize("products", [["sauce-labs-backpack", "sauce-labs-bike-light"]])
# def test_full_ecommerce_flow(driver, products):
#     login = LoginPage(driver)
#     inventory = InventoryPage(driver)
#     cart = CartPage(driver)

#     # 1. Login
#     login.login("standard_user", "secret_sauce")
#     assert "inventory" in driver.current_url
#     time.sleep(3)

#     # 2. Add multiple products
#     for product in products:
#         inventory.add_product_by_id(product)

#     # 3. Verify cart count
#     cart_count = inventory.get_cart_count()
#     assert cart_count == len(products), f"Expected {len(products)} items, got {cart_count}"
#     time.sleep(3)

#     # 4. Go to cart
#     inventory.go_to_cart()
#     cart_products = cart.get_all_products()
#     assert all(name for name in cart_products), "Cart should have all added products"
#     print("Products in cart:", cart_products)
#     time.sleep(3)

#     # 5. Remove first product
#     cart.remove_product_by_name(cart_products[0])
#     remaining_products = cart.get_all_products()
#     assert len(remaining_products) == len(products) - 1, "One product should be removed"
#     print("Products after removal:", remaining_products)
#     time.sleep(3)

#     # 6. Checkout simulation
#     cart.click_checkout()
#     assert "checkout-step-one" in driver.current_url, "Should navigate to checkout"
#     time.sleep(3)

#     # 7. Logout
#     inventory.logout()
#     assert "saucedemo.com" in driver.current_url
