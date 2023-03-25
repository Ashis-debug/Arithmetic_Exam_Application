text = input()
words = text.split()
for word in words:
    # finish the code here
    if word.startswith("WWW."):
        print(word)
    if word.startswith("www."):
        print(word)
    if word.startswith("https://"):
        print(word)
    if word.startswith("http://"):
        print(word)
