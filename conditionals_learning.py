def age_foo(age):
    new_age = age + 50
    return new_age

wiek=float(input("Enter your age: "))

if wiek > 150:
    print("Are you sure?")
else:
    print(age_foo(wiek))