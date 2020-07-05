def show_magicians(magicians_name):
    for name in magicians_name:
        print(name)

def make_great(magicians_name):
    for i in range(len(magicians_name)):
        magicians_name[i] = 'The Great ' + magicians_name[i]
    return magicians_name

magicians_name_0 = ['aaa', 'bbb', 'ccc']
magicians_name_1 = make_great(magicians_name_0[:])
show_magicians(magicians_name_0)
show_magicians(magicians_name_1)