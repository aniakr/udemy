file=open('C:/Users/Ania/PycharmProjects/test1/udemy/file_to_handle','r')
content=file.read()
print (content)
file.seek(0)
content_line=file.readlines()
content_line=[i.rstrip("\n") for i in content_line]
print(content_line)
file.close()

fruits_file=open('C:/Users/Ania/PycharmProjects/test1/udemy/fruits.txt','r')
fruits_content=fruits_file.read()
#fruits_file.close()
print(fruits_content)

fruits_file.seek(0)
fruits_len_line=fruits_file.readlines()
# fruits_len_line=[len(i)-1 for i in fruits_len_line]
# print(fruits_len_line)
fruits_file.close()

for i in fruits_len_line:
    print(len(i.strip()))

for i in fruits_len_line:
    fruits_len_line = fruits_file.read()
    fruits_len_line=fruits_len_line.splitlines()
    print(i)

# to lepiej, bo nie wyswietla listy tylko po kolei w nowych liniach