def make_album(artist, album):
    """Return dictionary of album"""
    full_album = {'artist': artist, 'album': album}
    return full_album

while True:
    print("\nPlease tell me artist and album:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    album = input("Album: ")
    if album == 'q':
        break

    formatted_album = make_album(artist, album)
    print(formatted_album)