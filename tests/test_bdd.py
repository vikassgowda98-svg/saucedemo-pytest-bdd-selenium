from pytest_bdd import scenarios

# Smoke
scenarios("../features/smoke/login.feature")
scenarios("../features/smoke/end_to_end_smoke.feature")


# Sanity
scenarios("../features/sanity/application_sanity.feature")
scenarios("../features/sanity/logout_sanity.feature")


# Regression
scenarios("../features/regression/login_regression.feature")
scenarios("../features/regression/products_regression.feature")
scenarios("../features/regression/cart_regression.feature")
scenarios("../features/regression/checkout_regression.feature")