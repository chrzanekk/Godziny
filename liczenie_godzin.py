#simple script to count work hours
#now count only real time of work.
#in future i want to add some impruvements like date input with hours
#final job is to count work hours with additional hours and add 50% and 100% extra paymnet


def godziny(godz_pocz=None,godz_konc=None): 
    godz_pocz = int(input("Godzina rozpoczęcia pracy: "))
    godz_konc = int(input("Godzina zakończenia pracy: "))
    ilosc = godz_konc - godz_pocz
    print("Czas pracy to:",ilosc, "godzin")
    
godziny()
    
                    
