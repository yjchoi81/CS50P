import re
import sys


def main():
    try:

        user_input = user_input = input("Hours: ")
        result = convert(user_input)
        print(result)

    except ValueError:
        print("ValueError")
        sys.exit(1)


# Convert a 12-hour clock to a 24-hour clock
def convert(s):
    pattern = r"^(1[0-2]|[1-9])(?:(:[0-5]\d))?\s+([AP]M)\s+to\s+(1[0-2]|[1-9])(?:(:[0-5]\d))?\s+([AP]M)$"
    match = re.search(pattern, s, re.IGNORECASE) # re.IGNORECASE = case-insensitive comparisons

    if not match:
        raise ValueError

    start_h = int(match.group(1))
    end_h = int(match.group(4))
    amp1 = match.group(3)
    amp2 = match.group(6)

    if match.group(2) is None:
        start_m = 0 # Convert value ​​excluding colon(:) to int
    else:
        start_m = int(match.group(2)[1:])

    if match.group(5) is None:
        end_m = 0
    else:
        end_m = int(match.group(5)[1:]) # Convert value ​​excluding colon(:) to int

    if start_m >= 60 or end_m >= 60: # check for 60 min or more
        raise ValueError

    if amp1 == "PM":
        if 1 <= start_h <= 11:
            start_h += 12
    elif amp1 == "AM":
        if start_h == 12:
            start_h = 0

    if amp2 == "PM":
        if 1 <= end_h <= 11:
            end_h += 12
    elif amp2 == "AM":
        if end_h == 12:
            end_h = 0

        """if start_m == None: ## incorrect way (correct way : start_m is None)
            start_m = 00
        elif start_m >= 60:
            raise ValueError
        else:
            start_m = int(match.group(2)[1:])

        if end_m == None:
            end_m = 00
        elif end_m >= 60:
            raise ValueError"""

    return f"{start_h:02}:{start_m:02} to {end_h:02}:{end_m:02}"





if __name__ == "__main__":
    main()
