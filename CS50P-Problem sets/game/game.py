import random

while True:
    try:
        n = int(input('Level: '))
        #if n < 0:
            #pass
        if n > 0:
            break
    except ValueError:
        pass

com = random.randint(1,n)
#print(com)

while True:
    try:
        guess = int(input('Guess: '))
        if guess > 0:
            if guess < com:
                print("Too small!")
            elif guess > com:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass



