def show_magicians(magicians_name):
    for name in magicians_name:
        print(name)

def make_great(magicians_name):
    for i in range(len(magicians_name)):
        magicians_name[i] = 'The Great ' + magicians_name[i]

magicians_name = ['aaa', 'bbb', 'ccc']
make_great(magicians_name)
show_magicians(magicians_name)
