import validators

def main():
    email = input("What's your email address? ")
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()

"""다음을 사용하여 validator-collection을 설치할 수 있습니다.
pip install validator-collection

다음을 사용하여 검증기를 설치할 수 있습니다.
pip install validators """
