# Funkcja potegowanie
def raise_to_power(base_number, power_number):
    result = 1

    for index in range(power_number):
        result = result * base_number

    return result


print(raise_to_power(2, 3))
print(raise_to_power(3, 2))
print(raise_to_power(5, 0))
# Cwiczenie na potegowanie , dziala bo mimoiz powe_number jest konczony o 1 wartosc wczesniej to zczynamy iteracje od 0 i jest ok
