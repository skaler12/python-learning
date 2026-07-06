price = 2499.99
discount = 300
quantity = 2

final_price = price - discount
total_price = final_price * quantity

print("Cena produktu:")
print(price)

print("Rabat:")
print(discount)

print("Cena po rabacie:")
print(final_price)

print("Liczba sztuk:")
print(quantity)

print("Cena łączna:")
print(total_price)

print("Zaokrąglona cena łączna:")
print(round(total_price))

products = 17
package_size = 5
print(products % package_size)
