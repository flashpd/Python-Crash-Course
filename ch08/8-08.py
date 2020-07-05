def make_album(singer_name, album_name, song_num = ''):
    albums = {'singer_name': singer_name, 'album_name: ': album_name, 'song_num': song_num}
    return albums

while 1:
    singer_name = input("Please input a singer name: ")
    album_name = input("Please input an album name: ")
    song_num = input("Please input songs number: ")
    
    album_0 = make_album(singer_name, album_name, song_num)
    print(album_0)

    flag = input("Again?(Enter yes or no) ")
    if flag == 'no':
        break