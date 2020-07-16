file_name = 'learning_python.txt'
with open(file_name) as file_object:
    content_0 = file_object.read()
    print(content_0)
print("-----")

with open(file_name) as file_object:
    line = file_object.readline()
    print(line)
print("-----")

with open(file_name) as file_object:
    lines = file_object.readlines()

print(lines)

