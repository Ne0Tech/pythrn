age = int(input("Enter your age: "))

if age < 5:
    print("You should play with toys.")
elif 5 <= age <= 12:
    print("You can play outdoor games.")
elif 13 <= age <= 17:
    print("You can play video games.")
else:
    age >= 18
    print("You could try hiking. ")