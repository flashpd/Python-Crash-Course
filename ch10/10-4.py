filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while 1:
        name = input('Please input your name(Press q to exit): ')
        if name == 'q':
            break
        else:
            name = name + '\n'
            file_object.write(name)