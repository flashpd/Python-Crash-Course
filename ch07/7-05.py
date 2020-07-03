while 1:
    age = input("Please input one age: ")
    if age >= 3 & age <= 12:
        print("Price: $10")
    elif age > 12:
        print("Price: $15")
    else:
        print("free")