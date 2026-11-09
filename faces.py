def convert(string):
    return (string.replace(":)", "🙂").replace(":(", "🙁"))

def main():
    emoticon = (input("Type anything."))
    emoji = convert(emoticon)
    print(emoji)

main()