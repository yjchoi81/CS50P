import csv
import sys
from tabulate import tabulate

def main():

    read_file = sys.argv[1]

    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if not read_file.endswith('.csv'):
        sys.exit('Not a CSV file')


    try:
        with open(read_file, 'r', newline= '') as f:
            menu = csv.reader(f)
            menu_print =[]
            for row in menu:
                menu_print.append(row)
                print(tabulate(menu_print, tablefmt="grid", headers = 'firstrow'))


    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
