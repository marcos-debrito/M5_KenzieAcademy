from menu import products


def get_product_by_id(id: int):

    if type(id) != int:
        raise TypeError("product id must be an int")

    for product in products:
        if (product["_id"] == id):
            return product
    return {}


def get_products_by_type(string):

    if type(string) != str:
        raise TypeError("product type must be a str")

    array = []
    for product in products:
        if (product["type"] == string):
            array.append(product)
    return array


def add_product(menu, **kwargs: dict):
    new_id = 1
    if len(menu) > 0:
        menu_sorted = sorted(menu, key=lambda x: x["_id"])
        last_id = menu_sorted[-1]["_id"]
        new_id = last_id + 1  # 103
    newProduct = kwargs
    newProduct["_id"] = new_id
    menu.append(newProduct)
    return newProduct


def menu_report():

    product_count = len(products)

    total_price = 0
    for product in products:
        total_price += product["price"]

    average_price = round(total_price / product_count, 2)

    products_counts = {}

    for product in products:
        product_type = product["type"]
        if product_type in products_counts:
            products_counts[product_type] += 1
        else:
            products_counts[product_type] = 1

    most_common_type = ""
    highest = 0
    for key, value in products_counts.items():
        if value > highest:
            highest = value
            most_common_type = key

    string = f"Products Count: {product_count} - "
    string += f"Average Price: ${average_price} - "
    string += f"Most Common Type: {most_common_type}"
    return string
