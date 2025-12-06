def main():
    convert_time = convert(input("what time is it? "))
    if 7.0 <= convert_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert_time <= 13.0:
        print("lunch time")
    elif 18.0 <= convert_time <= 19.0:
        print("dinner time")
    else:
        print("")


def convert(time):
    time = time.lower().replace("am", "").replace("pm", "")
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    total_hours = hours + minutes/60
    return total_hours


if __name__ == "__main__":
    main()
