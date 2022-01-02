request = False

print("Enter the number of hours this month, this way :")
while request is False :
    try :
        time = input("hours.minutes\n")
        hours, minutes = time.split(".")

        hours = int(hours)
        minutes = int(minutes)

        request = True

    except :
        print("Please enter a number")
        request = False

request = False

time_in_hours = hours + (minutes / 60)

time_this_month = time_in_hours / 730 * 100
time_this_month = round(time_this_month, 2)

print(f"You spent {time_this_month}% of your time behind your phone this month")

time_in_life = time_this_month/100 * 77
time_in_life = round(time_in_life, 2)

print(f"If you continue this way, you'll spend {time_in_life} years behind your phone in your life")



while request is False :
    try :
        unlocks = int(input("Enter the number of unlocks this month\n"))
        request = True

    except :
        print("Please enter a number")
        request = False

request = False

unlocks_this_month = unlocks / 730
unlocks_this_month = round(unlocks_this_month, 2)

print(f"You unlocked your phone {unlocks_this_month} times per hours this month")

unlocks_this_month_frequency = 60 / unlocks_this_month
unlocks_this_month_frequency = round(unlocks_this_month_frequency, 2)

print(f"That means that you unlocked your phone each {unlocks_this_month_frequency} minutes")