integer_1 = input("Please input a integer: ")
integer_2 = input("Please input a integer: ")

try:
    sum_0 = int(integer_1) + int(integer_2)
except ValueError:
    print("Please input integers.")
else:
    print(sum_0)
