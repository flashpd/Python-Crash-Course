filename = 'Python-Crash-Course\guest.txt'

name = input('Please input your name: ')
with open(filename, 'w') as file_object:
    file_object.write(name)