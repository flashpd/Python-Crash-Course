def read_txt(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            print(contents)
    except FileNotFoundError:
        pass

filename_1 = 'cat.txt'
filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'

read_txt(filename_1)
read_txt(filename_2)