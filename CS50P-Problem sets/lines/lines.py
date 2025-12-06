import sys

def main():
    # To check one command-line argument and that file’s name ends in '.py'
    if len(sys.argv) > 2:
            sys.exit("Too many arguments")
    if len(sys.argv) < 2:
            sys.exit("Too few arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


# To count lines in the file
    try:
        with open(sys.argv[1]) as file:
            count_line = 0
            for line in file:
                cleaned_line = line.lstrip()
                if not cleaned_line.startswith("#") and cleaned_line != "":
                    count_line += 1
            print(count_line)

# To check if the file does not exist
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
