def make_album(artist, title, songs=None):
    album_dict = {
        "artist": artist.title(),
        "title": title.title(),
    }
    if songs:
        album_dict['songs'] = songs
    return album_dict


artist_prompt = "What is the name of the artist? "
title_prompt = "What is the album title? "

print("Enter 'quit' any time to stop. ")

while True:
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    title = input(title_prompt)
    if title == 'quit':
        break
    songs = input("How many songs on the album? if unknown leave blank and press 'enter' ")
    if songs == 'quit':
        break
    album = make_album(artist, title, songs)
    print(album)
