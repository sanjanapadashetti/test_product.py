from product import get_product_info

def test_product_info():
    expected_output = (
        "Product ID: K193\n"
        "Name: KitKat\n"
        "Quantity: 40g\n"
        "Price: 20\n"
    )

    assert get_product_info("K193", "KitKat", "20", 40g) == expected_output
