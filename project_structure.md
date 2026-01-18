1. High-Level Project Structure

SauceDemo/
│
├── pages/
│   ├── login_page.py               --> Handles all interactions related to the login page.
│   ├── inventory_page.py           --> Handles product listing and header-related actions.
│   ├── cart_page.py                --> Handles cart page, checkout, shipping and order completion.
│
├── tests/
│   ├── test_login.py               --> Validates login for multiple user types.
│   ├── test_cart_badge.py
│   ├── test_cart_flow.py           --> Validate add to cart, remove from car
│   ├── test_full_flow.py           --> Validates: Login, add items, cart badge, remove item, checkout, shipping, finish order, logout, performance
│
├── utils/
│   └── utils_performance_test.py   --> Measures time-based performance metrics.
│
├── conftest.py                     --> Manages pytest fixtures
├── pytest.ini                      --> Pytest configuration
└── requirements.txt
