

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # 1. 길이 확인
    if not (2 <= len(s) <= 6):
        return False

    # 2. 첫 두 글자 확인
    if not s[:2].isalpha():
        return False

    # 3. 문자/숫자만
    if not s.isalnum():
        return False

    # 4 & 5. 숫자 규칙 확인
    for i, ch in enumerate(s):
        if ch.isdigit():
            # 첫 숫자가 0이면 안 됨
            if ch == '0':
                return False
            # 숫자 이후에 문자가 있으면 안 됨
            if not s[i:].isdigit():
                return False
            break  # 이후는 검사할 필요 없음

    return True


if __name__ == "__main__":
    main()
