#simple script to count work hours
#you can input date. i use it to check what day of week it is and coresponding to that day cout and addition to payment
#final versioncount work hours with additional hours and add 50% and 100% extra payment.


import calendar
import datetime


def date_time_input():
    try:
        date_entry = input("Input date and time in DD/MM/YYYY/HH/MM format: ")
        day, month, year, hour, minutes = map(int, date_entry.split("/"))
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day), int(hour), int(minutes))
        except ValueError:
            isValidDate = False
        if(isValidDate):
            print("Entered date and time is valid.")
            date_time = [day, month, year, hour, minutes]
            return date_time
        else:
            print("Entered date and time is not valid. Try again.")
            pass


    except ValueError:
        print("Incorrect format.")


# #simple function that convert inputed date to day of week
def check_date(y, m, d):
    day_of_week = calendar.weekday(y, m, d)
    day_of_week_dict = {0: "Monday/Poniedziałek",
                        1: "Tuesday/Wtorek",
                        2: "Wednesday/Środa",
                        3: "Thursday/Czwartek",
                        4: "Friday/Piątek",
                        5: "Saturday/Sobota",
                        6: "Sunday/Niedziela"}
    k = 0
    for k in day_of_week_dict:
        if k == day_of_week:
            # print(day_of_week_dict[k])
            break
    return day_of_week_dict[k]

def hours(d1, d2, m1, m2, h1, h2, min1, min2):
    hour_count = 0
    if (d1 < d2 and m1 == m2) or (d1 > d2 and m1 < m2):
        if min1 < min2:
            hour_count = 24 + h2 - h1 + 0.5
        elif min2 < min1:
            hour_count = 24 + h2 - h1 - 0.5
        elif min2 == min1:
            hour_count = 24 + h2 - h1
        return hour_count
    elif d1 == d2 and m1 == m2:
        if min1 < min2:
            hour_count = h2 - h1 + 0.5
        elif min2 < min1:
            hour_count = h2 - h1 - 0.5
        elif min2 == min1:
            hour_count = h2 - h1
        return hour_count


print("HOUR COUNTER 2019 - by K. Chrzanowski")
print("-------------------------------------")
print("Simple script to count extra hours of work")
print("depending by day and hours. Script check what ")
print("day of week was from entered date and time and")
print("then use appriopriate function.")
print("Key: ")
print("Mon - Fri: 0-8h = +0%, 9-10h = +50%, >10h = +100%")
print("Saturday: all day + 50%")
print("Sunday: all day +100%")
print("-------------------------------------")
print("Start work:")
date1 = date_time_input()
try:
    what_day1 = check_date(date1[2], date1[1], date1[0])
    # print(what_day1)
except TypeError:
    print("Check date/format and try again.")
print("End work:")
date2 = date_time_input()
try:
    what_day2 = check_date(date2[2], date2[1], date2[0])
    # print(what_day2)
except TypeError:
    print("Check date/format and try again.")


#code for counting hours from date and time entered above.
try:
    print("Start work at: ", what_day1)
    print("End work at: ", what_day2)
    start_day = date1[0]
    start_month = date1[1]
    start_hour = date1[3]
    start_min = date1[4]
    end_day = date2[0]
    end_month = date2[1]
    end_hour = date2[3]
    end_min = date2[4]
    hours1 = hours(start_day, end_day, start_month, end_month, start_hour, end_hour, start_min, end_min)
    print("Ilość przepracowanych godzin: ", hours1)
except NameError:
    print("ERROR! Something goes wrong. Check input data again.")




