import numpy as np
import pandas as pd
import time
import datetime

#My sincere gratitude to stand on the shoulders of countless giants whom have established the foundation for me to learn from

def select_day():
    day = input("Which day of the week?  Monday 1,  Tuesday 2, Wednesday 3, Thursday 4, Friday 5, Saturday 6, Sunday 7")
    return day

def select_time_period():
    """Prompt the end-user for the specific time-period and return the requested data (amongst these three cities)
    Args:
        none.
    Returns:
#TO DO: fill out and return the associated data type and the appropriate, description (examples: select_city, select_month, etc.)
    """
    time_period = input('\nWould you like to display the results by the month, day, or not at'
                        ' all? Enter "none" if you do not what to use a time-filter.\n')

    return time_period

def select_city():
    """Prompt the end-user for the specific city and return the appropriate filename for the designated city's bikeshare data (amongst these three cities)
    Args:
        none.
    Returns:
        (str) filename for the respective city's bikeshare data (chicago, new york city, washington)
    """
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see the data for Chicago, New York City, or Washington?\n')

#TO DO: process the input request and display the appropriate, requested information (amongest these three cities)

    if city.title() == "chicago":
        data = "chicago"
    elif city.title() == "new york city":
        data = "new_york_city"
    else:
        data = "washington"

    return data

def select_month():
    month_input_raw = input('\nWhich month (between January and June?) January, February, March, April, May, or June?\n')
    if month_input_raw == "january":
        month_input = "01"
    elif month_input_raw =="february":
        month_input = "02"
    elif month_input_raw == "march":
        month_input ="03"
    elif month_input_raw == "april":
        month_input ="04"
    elif month_input_raw == "may":
        month_input ="05"
    else:
        month_input = "06"
    return month_input

#Amongst these three cities, which city has the most popular, bikeshare, start-time?

def popular_start_time(file, the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        best_hour_dict = {"00":0,"01":0,"02":0,"03":0,"04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0,"19":0,"20":0,"21":0,"22":0,"23":0,"24":0}
        popular_hour_count = 0
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            hour = datetime.datetime.strftime(dt_obj, "%H")
            weekday = dt_obj.isoweekday()
            month = datetime.datetime.strftime(dt_obj, "%m")

            if the_month == month:
               for i in best_hour_dict:
                   if hour == i:
                       best_hour_dict[i] +=1

                   if popular_hour_count < best_hour_dict[i]:
                       popular_hour_count = best_hour_dict[i]
                       most_popular_hour = i

            if the_month == "all":
               for i in best_hour_dict:
                   if hour == i:
                       best_hour_dict[i] +=1

                   if popular_hour_count < best_hour_dict[i]:
                       popular_hour_count = best_hour_dict[i]
                       most_popular_hour = i

    popular_hour = most_popular_hour
    return popular_hour

def duration_stats(file, the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)

#Amongst these three cities, which month has the most popular, bikeshare, start-time?
#def popular_month(file)

def popular_month(file):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)

        best_month_dict =  {"january": 0,"february": 0,"march": 0, "april":0, "may": 0,"june":0}
        most_rides = 0
        best_month = ""

        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            if month == "01":
                best_month_dict["january"] += 1
            elif month == "02":
                best_month_dict["february"] += 1
            elif month =="03":
                best_month_dict["march"] += 1
            elif month =="04":
                best_month_dict["april"] += 1
            elif month =="05":
                best_month_dict["may"] += 1
            elif month =="06":
                best_month_dict["june"] += 1

        for i in best_month_dict:
            while most_rides < best_month_dict[i]:
                most_rides = best_month_dict[i]
                best_month = i

    return best_month

#Amongst these three cities, which day of the week has the most popular, bikeshare, start-time?

def most_popular_day_of_week(file, the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        weekday_dict = {"monday":0,"tuesday":0,"wednesday":0,"thursday":0,"friday":0,"saturday":0,"sunday":0}
        popular_weekday = ""
        count = 0
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            if month == the_month:
                if weekday == 1:
                    weekday_dict["monday"] += 1
                elif weekday == 2:
                    weekday_dict["tuesday"] += 1
                elif weekday == 3:
                    weekday_dict["wednesday"] += 1
                elif weekday == 4:
                    weekday_dict["thursday"] += 1
                elif weekday == 5:
                    weekday_dict["friday"] += 1
                elif weekday == 6:
                    weekday_dict["saturday"] += 1
                else:
                    weekday_dict["sunday"] += 1
            elif the_month == "all":
                if weekday == 1:
                    weekday_dict["monday"] += 1
                elif weekday == 2:
                    weekday_dict["tuesday"] += 1
                elif weekday == 3:
                    weekday_dict["wednesday"] += 1
                elif weekday == 4:
                    weekday_dict["thursday"] += 1
                elif weekday == 5:
                    weekday_dict["friday"] += 1
                elif weekday == 6:
                    weekday_dict["saturday"] += 1
                else:
                    weekday_dict["sunday"] += 1

        for i in weekday_dict:
                if count < weekday_dict[i]:
                    count = weekday_dict[i]
                    popular_weekday = i

    return popular_weekday

#city_file = get_city()
#month = get_month()
#print(most_popular_day_of_week(city_file, month))

#Amongst these three cities, what is the total, bikeshare, trip-length and the average, bikeshare, trip-length?
#this file is based on the chicago, new york city and washington city-data
#the_month = month_input(input from end-user)

        total_count = 0
        total_trip_length = 0
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()

            if the_month == month:
                total_count += 1
                trip = int(rows["Trip Length"])

                total_trip_length += trip

            elif the_month == "all":
                total_count += 1
                trip = int(rows["Trip Length"])
                total_trip_length += trip

    return total_trip_length, total_count

#Amongst these three cities, what is the most popular, bikeshare, start-station and the most popular, bikeshare, end-station?

def most_popular_start_and_end_station(file, the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        start_station_dict = {}
        most_popular_start_station = ""
        most_popular_end_station = ""
        end_station_dict = {}
        start_station_count = 0
        end_station_count = 0
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            start_station = rows["Start Station"]
            end_station = rows["End Station"]
            if the_month == month:
                    if end_station in end_station_dict:
                        count = end_station_dict[end_station]
                        end_station_dict[end_station] = count +1
                    else:
                        end_station_dict[end_station] = 1

                    if start_station in start_station_dict:
                        count = start_station_dict[start_station]
                        start_station_dict[start_station] = count + 1
                    else:
                        start_station_dict[start_station] = 1
            elif the_month == "all":
                    if end_station in end_station_dict:
                        count = end_station_dict[end_station]
                        end_station_dict[end_station] = count +1
                    else:
                        end_station_dict[end_station] = 1

                    if start_station in start_station_dict:
                        count = start_station_dict[start_station]
                        start_station_dict[start_station] = count + 1
                    else:
                        start_station_dict[start_station] = 1

        for i in start_station_dict:
            if start_station_count < start_station_dict[i]:
                start_station_count = start_station_dict[i]
                most_popular_start_station = i

        for j in end_station_dict:
            if end_station_count < end_station_dict[j]:
                end_station_count = end_station_dict[j]
                most_popular_end_station = j

    return most_popular_start_station, most_popular_end_station

#print(most_popular_start_and_end_station(city_file, month))
#print(most_popular_day_of_week(city_file, month))

#Amongst these three cities, what are the user-profile differences between one-off, bikeshare, customers and the regular, bikeshare, subscriber-base?

def user_type(file, the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        subscriber = 0
        customer = 0
        for rows in file:
            user = rows["User Type"]
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            if the_month == month:
                if user == "Subscriber":
                    subscriber += 1
                elif user == "Customer":
                    customer += 1
            elif the_month == "all":
                if user == "Subscriber":
                    subscriber += 1
                elif user == "Customer":
                    customer += 1

    return customer, subscriber

#Amongst these three cities, what are the, bikeshare, users' listed genders?

def gender_count(file, the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        female = 0
        male = 0
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            gender = rows["Gender"]
            if the_month == month:
                if gender == "Female":
                    female +=1
                elif gender == "Male":
                    male += 1
            elif the_month == "all":
                if gender == "Female":
                    female +=1
                elif gender == "Male":
                    male += 1

    return male, female

#print(gender_count(city_file, month_input))

#Amongst these three cities, who are the oldest (earliest) and youngest (latest) bikeshare users; and, what are the most popular bikeshare users' year of birth?

def birth_years(file, the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        birth_dict = {}
        birth_year_count = 0
        count = 0
        birth_years_list = []
        popular_years = ""

        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            weekday = dt_obj.isoweekday()
            if the_month == month:
                birth = rows["Birth Year"]

                if birth in birth_dict:
                    birth_year_count = birth_dict[birth]
                    birth_dict[birth] = birth_year_count + 1
                else:
                    birth_dict[birth] = 1

                    if birth not in birth_years_list and birth != "":
                        birth_years_list.append(birth)
            if the_month == "all":
                birth = rows["Birth Year"]

                if birth in birth_dict:
                    birth_year_count = birth_dict[birth]
                    birth_dict[birth] = birth_year_count + 1
                else:
                    birth_dict[birth] = 1

                    if birth not in birth_years_list and birth != "":
                        birth_years_list.append(birth)

        for i in birth_dict:
            if count < birth_dict[i] and i != "":
                count = birth_dict[i]
                popular_years = i
        oldest_year = min(birth_years_list)
        youngest = max(birth_years_list)

    return oldest_year, youngest, popular_years

def most_popular_trip(file, the_month):
    with open(file+".csv", 'r') as f_in:
        file = csv.DictReader(f_in)
        count = 0
        trip_count = 0
        trip_dict = {}
        for rows in file:
            date = rows['Start Time']
            dt_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            month = datetime.datetime.strftime(dt_obj, "%m")
            st_station = rows["Start Station"]
            en_station = rows["End Station"]
            trip = st_station +" -- "+ en_station
            if the_month == month:
                if trip in trip_dict:
                    count += 1
                    trip_dict[trip] = count
                else:
                    trip_dict[trip] = 1
            elif the_month == "all":
                if trip in trip_dict:
                    count += 1
                    trip_dict[trip] = count
                else:
                    trip_dict[trip] = 1

        for i in trip_dict:
            if trip_count < trip_dict[i]:
                trip_count = trip_dict[i]
                popular_trip = i
    return popular_trip

def statistics():
    """Calculate and display descriptive statistics for a given time period amongst these three cities
    Args:
        none.
    Returns:
        none.
    """
#Filter the data by the city (chicago, new york city, washington)
    city = pick_city()

#Filter the data by the time period (month, day, none)
    time_period = get_time_period()
    if time_period == "month":
        month_input = get_month()
        day = "ads"
    elif time_period == "none":
        month_input = "all"
        day = "ads"
    elif time_period == "day":
        month_input = "ads"
        day = get_day()

    print('Calculating the first statistic...')
    start_time = time.time()

#Amongst these three cities, what is the most popular, bikeshare, weekday start-time (monday, tuesday, etc.)?

    if time_period == 'none' or time_period == 'month':
        popular_day = most_popular_day_of_week(city, month_input)
        print("The most popular_day for start time is:{}".format(popular_day))
        #TO DO: request popular_day function and display the appropriate results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

#Amongst these three cities, what is the most popular, bikeshare, hour of the day start-time?
#TO DO: request popular_hour function and display the appropriate results

    hour = popular_start_time(city, month_input)
    print("The most popular bikeshare hour is:{}".format(hour))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

#Amongst these three cities, what is the most popular, bikeshare, monthly start-time?

    if time_period == 'none':
        most_popular_month = popular_month(city)
        print("The most popular bikeshare monthly, start-time is:{}".format(most_popular_month))

#TO DO: request popular_month function and display the appropriate results

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
    start_time = time.time()

#Amongst these three cities, what is the most popular, bikeshare, start-station and the most popular, bikeshare, end-station?
#TO DO: request most popular_stations function and display the appropriate results

    starting_station, ending_station = most_popular_start_and_end_station(city, month_input)
    print("The most popular, bikeshare, start-station is:{}".format(starting_station))
    print("The most popular, bikeshare, end-station is:{}".format(ending_station))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

#Amongst these three cities, what are the overall, bikeshare, trip-lengths and average, bikeshare, trip-lengths?
#TO DO: request trip_length function and display the appropriate results

    trip_duration, total = duration_stats(city, month_input)
    print("The overall, bikeshare, trip length is :{}".format(trip_duration))
    print("The average, bikeshare, trip length is :{}".format(trip_duration/total))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

#Amongst these three cities, what is the most popular overall, bikeshare, trip?
#TO DO: request popular_trip function and display the appropriate results

    popular_trip = most_popular_trip(city, month_input)
    print("most_popular_trip is:{}".format(popular_trip))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

#Amongst these three cities, what is the, bikeshare, users' listed gender?
#TO DO: request gender function and display the results
    #NOTE: Should a non-binary gender option and/or non-binary gender options be included?

    if city == "chicago" or city == "new_york_city":
        female, male = gender_count(city, month_input)
        print("total males:{}".format(male))
        print("total females:{}".format(female))

#Amongst these three cities, what are the oldest, youngest, and most popular years of birth?
#TO DO: request birth_years function and display the appropriate results

        print("Calculating the next statistic...")
        start_time = time.time()
        oldest, youngest, most_popular = birth_years(city, month_input)
        print("The oldest birth year is:{}".format(oldest))
        print("The youngest birth year is:{}".format(youngest))
        print("The most popular year of birth is:{}".format(most_popular))

        print("That took %s seconds." % (time.time() - start_time))

#Amongst these three cities, what are the listed, bikeshare, user-categories?
#TO DO: request users function and display the appropriate results

    customer, subscriber = user_type(city, month_input)
    print("The total number of, bikeshare, customers is:{}".format(customer))
    print("The total number of, bikeshare, subscribers is:{}".format(subscriber))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

#Amongst these three cities, what if the end-user decides to restart this program by returning to the beginning?
#TO DO: Provide the end-user with the following prompt

    restart = input('Would you like to restart this program by returning to the beginning? Type \'yes\' or \'no\'.')
    if restart.lower() == 'yes':
        statistics()

if __name__ == "__main__":
	statistics()
   
