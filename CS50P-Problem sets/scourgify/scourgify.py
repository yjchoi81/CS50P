import sys
import csv

#read_file = sys.argv[1]
#write_file = sys.argv[2]

# To seperate first name and last name
# write the first name, last name and house in a new file
# To check invalid file
def first_last_name(read_file, write_file):
    try:
        with open(read_file, "r") as rfile, open(write_file, "w", newline='') as wfile:
            reader = csv.DictReader(rfile)
            writer = csv.DictWriter(wfile, fieldnames=["first","last","house"])
            writer.writeheader()

            for row in reader:
                if "name" in row:
                    last, first = row["name"].split(",")
                else:
                    first = ""
                    last = ""

                writer.writerow({
                    "first":first.strip(),
                    "last":last.strip(),
                    "house":row["house"]})


    except FileNotFoundError:
        sys.exit(f"Could not read {read_file}")

# To check command-line arguments
def main():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    read_file = sys.argv[1]
    write_file = sys.argv[2]

    if not read_file.endswith('.csv') or not write_file.endswith('.csv'):
        sys.exit('Not a CSV file')

    first_last_name(read_file, write_file)



if __name__ == "__main__":
    main()
