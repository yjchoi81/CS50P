user_input = input("Expression: ")
x,y,z = user_input.split(' ')
x = int(x)
z = int(z)

if y == '+':
    print(float(x+z))
elif y == '-':
    print(float(x-z))
elif y == '*':
    print(f"{(x*z):.1f}")
else:
    print(f"{(x/z):.1f}")
