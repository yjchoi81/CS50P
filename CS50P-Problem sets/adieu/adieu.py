import inflect
p = inflect.engine()
name_list = []

while True:
    try:
        name = input('Name: ').title()
        name_list.append(name)

    except EOFError:
        print("")
        break

print(f'Adieu, adieu, to {p.join(name_list)}')


