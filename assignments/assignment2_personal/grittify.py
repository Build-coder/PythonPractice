#!/usr/bin/env python
import csv
from datetime import datetime
from sys import argv
# from music import Album, Song
import calendar

class Album: 
  
    # default constructor 
    def __init__(self, album_title, album_id, release_date, songs): 
        self.album = album_title
        self.id = album_id
        self.date = release_date
        self.songs = songs
  
    # a method for printing data members 
    def print(self): 

        year = self.date[0]
        month = convert_month(self.date[1])
        day = self.date[2]

        print(self.album + " by deadmau5, released on " + month
        + " " + day + ", " + year)

class Song:

    # default constructor
    def __init__(self, track_name, track_id, album_id):
        self.song = track_name
        self.id = track_id
        self.album = album_id

    # a method for printing data members
    def print(self):
        print(self.song)

# # save data string in album object
# album = Album(album[0] + " by deadmau5, released on "
# + month + " " + day + ", " + year)


def convert_month(month):

    month = int(month)

    year = {
        1 : 'January',
        2 : 'February',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8: 'August',
        9 : 'September',
        10 : 'October',
        11 : 'November',
        12 : 'December'
    }

    return year[month]
        


def get_all_albums():

    albums = []

    with open('deadmau5_albums.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"') 

        # counter
        count = 0

        for album in reader:

            # skip first line with metadata info
            if count > 0:
                date = album[2]
                date = date.split("-")
            
                # save data string in album object
                album = Album(album[0], album[1], date, "")

                albums.append(album)

            #increment counter
            count += 1  
    
    csvfile.close()

    # with open('deadmau5_tracks.csv', newline='') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    #     for songs in reader:

    #         # skip first line with metadata info
    #         if count > 0:
    #             song = songs[1]

    #             # save data string in album object
    #             songs = Album(

    #             albums.append(album)

    #         #increment counter
    #         count += 1  
    
    # csvfile.close()            

    return albums


def get_songs_by_date(after=True):

    if len(argv) < 4:

        raise ValueError("use is python3 grittify.py album [album-name]")

    date_object = datetime.strptime(argv[3], '%m/%d/%Y')
    albums = get_all_albums()

    for album in albums:

        for song in album.songs:

            if after and song.after(date_object):
                song.print()

            if not after and song.before(date_object):
                song.print()



if __name__ == '__main__':

    
    if len(argv) < 2:
        raise ValueError("use is python3 grittify.py [command] [args]")

    if argv[1] == 'albums':

        albums = get_all_albums()

        for album in albums:
            album.print()

    elif argv[1] == 'album':

        if len(argv) < 3:
            raise ValueError("use is python3 grittify.py album [album-name]")

        albums = get_all_albums()
        album_name_param = argv[2]
        print("The songs on {} are:".format(album_name_param))

        for album in albums:

            if album.name == album_name_param:

                for song in album.songs:
                    song.print()

    elif argv[1] == 'songs' and len(argv) == 2:

        albums = get_all_albums()

        for album in albums:

            for song in album.songs:
                song.print()

    elif argv[1] == 'songs' and argv[2] == "after":

        get_songs_by_date(True)

    elif argv[1] == 'songs' and argv[2] == "before":

        get_songs_by_date(False)

    else:
        raise ValueError("use is python3 grittify.py [command] [args]")