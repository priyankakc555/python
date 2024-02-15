with open("message.txt","r+")as fp:
    fp.write("Hello World")
    fp.seek(0)
    content=fp.read()

    print(content)
    