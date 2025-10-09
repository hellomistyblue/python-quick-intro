shopping_cart_items = [{"name": "thing", "price": 7},
                       {"name": "thing2", "price": 2}]

def average_price(cart_items):
    try:
        average = 0

        for item in cart_items:
            average += item["price"]

        average = average / len(cart_items)

        return average
    
    except Exception as exception:
        print(f"Exception type: {type(exception).__name__}")
        print(f"Exception message: {exception}")

average_price_of_cart_items = average_price(shopping_cart_items)

print(f"Your average cart item price is {average_price_of_cart_items} dollars")

