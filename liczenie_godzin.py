#simple script to count work hours
#now count only real time of work.
#in future i want to add some impruvements like date input with hours
#final job is to count work hours with additional hours and add 50% and 100% extra paymnet

import calendar


#simple function that convert inputed date to day of week
def input_date():
    d = int(input("Input day/Podaj dzień: "))
    m = int(input("Input month/Podaj miesiac: "))
    y = int(input("Input year/Podaj rok: "))
    day_of_week = calendar.weekday(y, m, d)
    day_of_week_dict = {0: "Monday/Poniedzialek",
                        1: "Tuesday/Wtorek",
                        2: "Wednesday/Środa",
                        3: "Thursday/Czwartek",
                        4: "Friday/Piątek",
                        5: "Saturday/Sobota",
                        6: "Sunday/Niedziela"}
    for k in day_of_week_dict:
        if k == day_of_week:
            print(day_of_week_dict[k])
            break


    #print(day_of_week)
    return day_of_week


#simple function that convert inputed date to day of week
def godziny():
    godz_pocz = int(input("Godzina rozpoczęcia pracy: "))
    godz_konc = int(input("Godzina zakonczenia pracy: "))
    ilosc = godz_konc - godz_pocz
    print("Czas pracy to:",ilosc, "godzin")
    return ilosc


godziny()
input_date()
    

