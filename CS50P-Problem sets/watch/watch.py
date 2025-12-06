import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    pattern = r'<iframe\s+[^>]*src\s*=\s*["\'](?:https?://)?(?:www\.)?(?:youtube\.com|youtu\.be)/(?:embed/|watch\?v=)?([\w-]+)["\']'
    match = re.search(pattern, s, re.S)

    if match:
        url = match.group(1)
        final_url = f"https://youtu.be/{url}"
        return final_url

    else:
        return f"None"

...


if __name__ == "__main__":
    main()
