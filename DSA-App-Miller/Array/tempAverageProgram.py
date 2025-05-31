def temperatureAvg():
    count = 0
    temp_list = []
    inp_days = int(input("Enter the number of days you want to calculate: "))
    for i in range(inp_days):
        day_temp = int(input(f"Enter the day {i+1} temperature: "))
        temp_list.append(day_temp)
    average = sum(temp_list) / inp_days
    print(f"Average: {average}")
    for i in temp_list:
        if i > average:
            count += 1
    print(f"{count} day(s) above the average")


temperatureAvg()
