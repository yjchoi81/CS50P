import re
import sys


def main():
    user_input = input("Text: ")
    result = count(user_input)
    print(result)


def count(s):
    pattern = r"\bum\b"
    # pattern = r".*\bum\b.*" for re.search and the count is always 1
    # pattern = r"\bum\b" for re.findall
    # re.findall find all 'um' and make a list
    match = re.findall(pattern, s, re.IGNORECASE)

    if match:
        c = len(match)

    return c

if __name__ == "__main__":
    main()
