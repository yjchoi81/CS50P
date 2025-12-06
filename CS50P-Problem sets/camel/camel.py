variables_names ={
    "name":"snake_name : name",
    "firstName":"snake_name : first_name",
    "preferredFirstName":"snake_name : preferred_first_name"
}

user_input = input("camelCase: ")

if user_input in variables_names:
    print(variables_names[user_input])
