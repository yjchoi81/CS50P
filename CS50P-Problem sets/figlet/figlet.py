import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


def main():
    f = None
    if len(sys.argv) ==3:
        if (sys.argv[1] == '-f' or sys.argv[1] =='--font') and sys.argv[2] in fonts:
            f = sys.argv[2]
        else:
            print('Invalid usage')
            sys.exit(1)
    elif len(sys.argv) == 1 :
        f = random.choice(fonts)
    else:
        print("Invalid usage")
        sys.exit(1)


    figlet.setFont(font=f)


    s = input('Input: ')
    print(f'Output: {figlet.renderText(s)}')

if __name__ == "__main__":
    main()
