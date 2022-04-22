def make_album(artist, album):
    album = {'name_artist': artist,
             'album': album
             }
    return album


def run():
    album_1 = make_album("Junior H", "Sueño")
    album_2 = make_album("Billie Eilish", "When we fall asleep ...")
    album_3 = make_album("TOP", "Trench")

    print(album_1)
    print(album_2)
    print(album_3)


if __name__ == "__main__":
    run()
