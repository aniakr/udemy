def divide(a,b):
    try:
        return a/b
    except:
        return "Some error"

print(divide("z",0))

def divide2(a,b):
    try:
        return a/b
    except (ZeroDivisionError, TypeError):
        return "Division byt zero!"

print(divide2("z",0))

