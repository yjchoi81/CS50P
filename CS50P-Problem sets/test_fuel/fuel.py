def main():
    while True:
        try:
            fraction_str = input("fraction: ")
            to_percentage = convert(fraction)
            fuel_gauge = gauge(percentage)
            print(fuel_gauge)
            break  # Exit the loop on successful conversion
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    fraction = fraction.split('/')
    x = int(fraction[0])
    y = int(fraction[1])
    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0:
        raise ValueError
    if x > y:
        raise ValueError
    if x != int(x) or y != int(y):
        raise ValueError
    return round(x/y*100)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"
    else:
        return str(percentage)+'%'


if __name__ == "__main__":
    main()

