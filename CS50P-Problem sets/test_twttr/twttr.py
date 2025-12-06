def main():
    user_input = shorten(input("Input: "))
    shorten(user_input)

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in word:
        if vowel.lower() in vowels:
            word = word.replace(vowel,"")

    return word


if __name__ == "__main__":
    main()
