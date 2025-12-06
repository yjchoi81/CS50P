import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_number = r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
     # r"^(?:[0-255]\.){3}[0-255]$" # "r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    pattern = rf"^{ip_number}\.{ip_number}\.{ip_number}\.{ip_number}$"
    match = re.search(pattern, ip)
    if match:
        return True
    else:
        return False



if __name__ == "__main__":
    main()
