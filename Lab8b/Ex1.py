# Calculating an extend price for a product (with tax)
product = {
    "name": "small gunball",
    "price": 0.34,
}

tax_rate = 0.45

total = product["price"] + (product["price"] * tax_rate)
print(f"{product['name']} cost ${total:.2f}")

