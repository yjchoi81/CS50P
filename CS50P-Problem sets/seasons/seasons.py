import sys
import inflect
from datetime import date

#main function to get user input and print total minutes lived
def main():
    try:
         birthday = input("Date of Birth: ")
         born = date.fromisoformat(birthday)
    except ValueError:
        sys.exit(1)

    age_in_minutes = calculate_total_minutes(born)
#format number in words
    age_in_minutes_str = inflect.engine().number_to_words(age_in_minutes, andword="")
    age_in_minutes_str = age_in_minutes_str.capitalize()
    print(f"{age_in_minutes_str} minutes")



#calculate age and calculate how many leap years have passed and calculate age to minutes
def calculate_total_minutes(born):
    today = date.today()
    time_difference = today - born

    #if born > today:
        #sys.exit()

    age_in_minutes = time_difference.days * 1440   # only consider full days for minute calculation

    return age_in_minutes


if __name__ == "__main__":
    main()

