file_created=open("file_to_handle2.txt",'w')
file_created.write("Line 1\n")
file_created.write("Line 2\n")
file_created.write("Line 3\nLine 4")
file_created.close()

numbers=[1,2,3]
file_123=open("file_to_handle2.txt",'w')
for i in numbers:
    file_123.write(str(i)+"\n")
file_123.close()

file_123=open("file_to_handle2.txt",'a')
file_123.write("Line adding")
file_123.close()