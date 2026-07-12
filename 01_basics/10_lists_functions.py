# Create simple list
friends = ["Adam", "Tomek", "Jurek", "Anna"]
print(friends)

# Dodanie do listy
friends.append("Maja")
print(friends)

# Znaleznie indeksu na ktoryhm jest dany przyjaciel
print(friends.index("Tomek"))

# Dodanie na konkretna pozycje przyjaciela
friends.insert(0, "Mariusz")
print(friends)

# Usuniecie pozycji z listy
friends.remove("Tomek")
print(friends)

# Sortowanie listy
friends.sort()
print(friends)

# Lista od tylu
friends.reverse()
print(friends)

# Skopiowanie listy
friends2sort_reverse = friends.copy()
print(friends2sort_reverse)

# Zliczenie ilosci pozycji
friends2sort_reverse.append("Mariusz")
ilosc_mariuszy = friends2sort_reverse.count("Mariusz")
print(ilosc_mariuszy)
