def convert(emoticons):
    emoticons = emoticons.replace(":)","😐")
    return emoticons

def main():
    user_input = input("")
    print (convert(user_input))


main()
