
from config.settings import STRIPE_API_KEY
import stripe
stripe.api_key = STRIPE_API_KEY

def create_product(product):
    """ Создание продукта в страйпе"""

    product = stripe.Product.create(name=product.title)
    return product


def create_price(amount):
    """ Создание цены в страйпе"""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product_data={"name": "Payment"},
    )
    return price

def create_link(price):
    """ Создание сессии на оплату  в страйпе"""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")