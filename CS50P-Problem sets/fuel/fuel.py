def main():
    fuel = fraction()
    print(fuel)

def fraction():
    while True:
        try:
            fuel = rate(input("fraction: "))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            return fuel


def rate(n):
    n = n.split('/')
    x = int(n[0])
    y = int(n[1])
    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0:
        raise ValueError
    if x > y:
        raise ValueError
    if x != int(x) or y != int(y):
        raise ValueError

    n = round(x/y*100)
    if n >= 99:
        n = "F"
        return n
    elif 0 <= n <= 1:
        n = "E"
        return n
    else:
        return str(n)+'%'


main()
