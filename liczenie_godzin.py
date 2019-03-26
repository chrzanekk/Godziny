#simple script to count work hours
#now count only real time of work.
#you can input date. i use it to check what day of week it is and coresponding to that day cout and addition to payment
#final job is to count work hours with additional hours and add 50% and 100% extra payment

import calendar

class setDateTime:
    def __init__(self, day, month, year, hour, minute):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute

    def setDate(self):
        InputDate = input("Set date in format DD/MM/YYYY: ")
        day, month, year = map(int, InputDate.split("/"))
        Date1 = {"Day: ": day, "Month: ": month, "Year: ": year}
        return Date1

    def setTime(self):
        InputTime = input("Set time in format HH:MM: ")
        hour, minutes = map(int, InputTime.split(":"))
        Time1 = {"Hour: ": hour, "Minutes: ": minutes}
        return Time1


# #simple function that convert inputed date to day of week
def check_date():
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
    return day_of_week


#simple function that convert inputed date to day of week
# def hours():
#     start_hour = int(input("Input start hour. / Godzina rozpoczęcia pracy: "))
#     end_hour = int(input("Input end hour. / Godzina zakonczenia pracy: "))
#     count = godz_konc - godz_pocz
#     print("Work time is / Czas pracy to:", count, "hours / godzin. ")
#     return ilosc






