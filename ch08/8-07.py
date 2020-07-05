def make_album(singer_name, album_name, song_num = ''):
    albums = {'singer_name': singer_name, 'album_name: ': album_name, 'song_num': song_num}
    return albums

album_0 = make_album('Zhoujielun', 'zhou', '100')
album_1 = make_album("Wanglihong", 'wang')
album_2 = make_album('Liuhuan', 'liu')

print(album_0)
print(album_1)
print(album_2)