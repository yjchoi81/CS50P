import random


def main():
    level = get_level()
    final_score = quiz_game(level)
    print(f"Score: {final_score}")


def get_level():
    while True:
        try:
            n = int(input('Level: '))
            if n in [1, 2, 3]:
                return n
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else: # level == 3
        return random.randint(100, 999)


def quiz_game(level):
    score = 0
    for _ in range(10):
        tries = 0
        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
                    if tries == 3:
                        print(f"{x} + {y} = {x + y}")
                        break
            except ValueError:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(f"{x} + {y} = {x + y}")
                    break
    return score

    """count = 0
    eee = 0
    while count != 10:
        while eee != 2:
            if level == 1:
                n_list = [random.randint(1,9) for _ in range(2)]
                q = input(f'{n_list[0]} + {n_list[1]} = ')

                if q == n_list[0] + n_list[1]:
                    count += 1
                else :
                    print('EEE')
                    count += 0
                    eee += 1
                    if eee == 2:
                        print(f'{n_list[0]} + {n_list[1]}')"""




if __name__ == "__main__":
    main()
