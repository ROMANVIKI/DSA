def timeConversion(s):
    hour = s[:2]
    clock_format = s[-2:]

    if clock_format == "PM":
        if s[:2] == "12":
            return s[:8]
        else:
            con_hour = int(hour)
            con_hour += 12

            x = s[3:8]
            return f"{con_hour}:{x}"

    if clock_format == "AM":
        if s[:2] == "12":
            con_hour = "00"
            x = s[3:8]
            return f"{con_hour}:{x}"
        else:
            return s[:8]


sol = timeConversion(s="04:59:59AM")
print(sol)
