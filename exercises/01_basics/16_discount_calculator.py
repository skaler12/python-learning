def calculate_price(price, discount):
    return price * (1 - (discount / 100))


product_price = float(input("Enter product price: "))
discount_percent = float(input("Enter discount percent: "))

final_price = calculate_price(product_price, discount_percent)
print("Final price: " + str(final_price))
