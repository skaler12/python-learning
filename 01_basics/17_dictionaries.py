month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# Wyswietl zawartosc z lklucza Jan
print(month_conversions["Jan"])
# metoda get do wyswietlania wartosci klucza
print(month_conversions.get("Feb"))
# metoda get do wyswietlania wartosci klucza , nie ma luv wiec jest none
print(month_conversions.get("Luv"))
# metoda get zw ratwoscia wskazana jak nie znajdzie klucza
print(month_conversions.get("Luv", "Not a valid key"))
