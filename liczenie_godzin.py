
godz_pocz = int(input("Godzina rozpoczęcia pracy: "))
godz_konc = int(input("Godzina zakończenia pracy: "))
ilosc = godz_konc - godz_pocz
print("Czas pracy to:",ilosc, "godzin")

day_of_week = int(input("Podaj numer dnia tygodnia (1-pon, 2-wt, 3-sr, 4-czw, 5-pt, 6-sb, 7-nd): "))
if day_of_week <=0 or day_of_week > 7: ## cheking if number is inputed correctly.
    while day_of_week > 7 or day_of_week <=0:
        day_of_week = int(input("BLAD. Podaj POPRAWNY numer dnia tygodnia (1-pon, 2-wt, 3-sr, 4-czw, 5-pt, 6-sb, 7-nd): "))


name_of_day = { "Poniedzialek" : 1, "Wtorek" : 2, "Sroda": 3, "Czwartek" : 4, "Piatek" : 5, "Sobota" : 6, "Niedziela" : 7} # names if the days in week and numer keys
# statement below is counting an multipiler of houres in weekend.
ilosc_godzin = 0
if day_of_week == 6:
    ilosc_godzin = ilosc * 1.5
elif day_of_week == 7:
    ilosc_godzin = ilosc * 2
else:

