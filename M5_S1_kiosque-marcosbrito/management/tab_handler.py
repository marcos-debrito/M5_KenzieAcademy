from menu import products


def calculate_tab(array):
    total = 0
    for order in array:
        for product in products:
            if order["_id"] == product["_id"]:
                price = product["price"]
                amount = order["amount"]
                total += price*amount
    total = round(total, 2)
    to_string = f"${total}"
    return {'subtotal': to_string}
