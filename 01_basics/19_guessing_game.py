# gra w zgadywanie - nauka petli while
proba = ""
numer_proba = 0
haslo = "giraffe"
limit_prob = 3
przegrana_gra = False

# dopoki probowane haslo rozne od hasla prawdziwego lub przegrana gra to falsz, wykouj petle
while proba != haslo and przegrana_gra:
    # Jezeli liczba prob mniejsza niz 3 to wpisuj haslo w innym wypadku blok else
    if numer_proba < limit_prob:
        proba = input("Wprowadz zgadywane haslo: ")
        numer_proba += 1
        # Zmiana statusu przegrana gra na wartos prawdziwa - true
    else:
        przegrana_gra = True
# Koniec petlli, psrawdzenie czy przegrana gra to tru w innym wypadku blok else
# Domyslenie to sorawdza czy true mozna tez napisac : przegrana_gra == True
if przegrana_gra:
    print("Niestety przegrales.")
else:
    print("Wygrales, gratulacje ")
