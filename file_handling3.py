with open("file_to_handle2.txt",'a+') as file123:
    file123.seek(0)
    file123.write("\nLine new")
    file123.seek(0)
    content=file123.read()

print (content)