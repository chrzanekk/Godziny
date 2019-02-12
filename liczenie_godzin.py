def godziny(godz_pocz=None,godz_konc=None):
    godz_pocz = int(input("Godzina rozpoczęcia pracy: "))
    godz_konc = int(input("Godzina zakończenia pracy: "))
    ilosc = godz_konc - godz_pocz
    print("Czas pracy to:",ilosc, "godzin")
    
godziny()
    
                    
