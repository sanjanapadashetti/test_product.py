def product_info(product_id, name, quantity, price):
    if not isinstance(quantity, int) or quantity <= 0:
        return "Error: Quantity must be a positive integer."

    return (
        f"Product ID: {product_id}\n"
        f"Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )


if __name__ == "__main__":
    product_id = "K193"
    name = "Kitkat"
    quantity = "40kg"   
    price = 20

    print("Product Details:\n")
    print(product_info(product_id, name, quantity, price))

