import re

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        num = input("Date: ").title().strip()

        # if num.isalpha() and 
        num = re.split('[,_/ -]+', num)

        if len(num) < 3:
            raise IndexError

        year = num[-1]
        day = num[1]
        month = num[0]

        if int(day) < 1 or int(day) > 31:
            raise ValueError

        if month in month_list:
            monthx = month_list.index(month) + 1
            print(f"{int(year)}-{monthx:02}-{int(day):02}")
            break

        elif int(month) < 1 or int(month) > 12:
            raise ValueError

        else:
            print(f"{int(year)}-{int(month):02}-{int(day):02}")
            break

    except (ValueError, IndexError):
        pass
