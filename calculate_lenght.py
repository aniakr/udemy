def lenght(string):
    return len(string)

word=input("Enter any word: ")
print("The word "+word+" has "+ str(lenght(word))+ " letters")


def lenght2(string):
    if type(string)==int:
        return "Int has no lenght"
    elif type(string)==float:
        return "Float has no lenght"
    else:
        return len(string)

print(lenght2(5))
