def timeConversion(s):
        # Write your code here
    time_list = []
    for i in s:
        time_list.append(i)
    hour = time_list[0]+time_list[1]
    am_pm= time_list[-2]+time_list[-1]
    minutes = time_list[3]+time_list[4]

    seconds = time_list[6]+time_list[7]
    if hour == '12' and am_pm == 'AM':
        hour = '00'

        return hour+':'+ minutes + ':' + seconds +am_pm
    
    elif am_pm == 'PM' or am_pm == 'pm':
        hour = int(hour)
        hour = hour + 12
        return str(hour)+':'+ minutes + ':' + seconds+am_pm
    else:
        return hour+':'+ minutes + ':' + seconds+am_pm

if __name__ == '__main__':
    

    s = input()

    result = timeConversion(s)
    print(result)
x = '07:05:45PM'








