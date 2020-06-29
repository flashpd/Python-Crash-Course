names = ['panda', 'tiger', 'bear']
message = 'Welcome '
names.insert(0, 'cattle')
names.insert(2, 'sheep')
names.append('pig')

print(message + names[0])
print(message + names[1])
print(message + names[2])
print(message + names[3])
print(message + names[4])
print(message + names[5])


message = 'Sorry '
temp_name = names.pop()
print(message + temp_name)

temp_name = names.pop(2)
print(message + temp_name)

temp_name = names.pop(3)
print(message + temp_name)

temp_name = names.pop(1)
print(message + temp_name)

message = 'Welcome '
print(message + names[0])
print(message + names[1])

del names[0]
del names[0]
print(names)