def minutes_to_hours(minutes, seconds):
    hours=minutes/60 + seconds/3600
    return hours


def minutes_to_hours2(seconds, minutes=60):
    hours=minutes/60 + seconds/3600
    return hours


def age_foo(age):
    new_age=float(age)+50
    return new_age


wiek=input("Enter your age: ")
print(age_foo(wiek))

