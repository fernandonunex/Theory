def make_album(artist, album):
    album = {'name_artist': artist,
             'album': album
             }
    return album


def run():
    # Exercise 8.7
    # album_1 = make_album("Junior H", "Sueño")
    # album_2 = make_album("Billie Eilish", "When we fall asleep ...")
    # album_3 = make_album("TOP", "Trench")

    # print(album_1)
    # print(album_2)
    # print(album_3)

    # Exercise 8.8

    while True:
        print("(enter 'q' to quit any time)")
        artist_name = input("Enter the artist name: ")
        album_name = input("Enter the album name: ")

        if artist_name == 'q' or album_name == 'q':
            break
        else:
            album_info = make_album(artist_name, album_name)
            print(album_info)


if __name__ == "__main__":
    run()
