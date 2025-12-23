from product import get_product_info

def test_product_info():
    expected_output = (
        "Product ID: P102\n"
        "Name: Keyboard\n"
        "Quantity: 5\n"
        "Price: 899.5\n"
    )

    assert get_product_info("P102", "Keyboard", 5, 899.5) == expected_output
