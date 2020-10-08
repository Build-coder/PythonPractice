#!/usr/bin/env python
import csv
from datetime import datetime
from sys import argv
# from music import Album, Song

class Album: 

    def __init__(self, album_title, album_id, release_date, songs): 
        self.name = album_title
        self.id = album_id
        self.date = release_date
        self.songs = songs
  
    # a method for printing data members 
    def print(self): 

        date = self.date.split("-")

        year = date[0]
        month = convert_month(date[1])
        day = date[2]

        print(self.name + " by deadmau5, released on " + month
        + " " + day + ", " + year)

class Song:

    def __init__(self, track_name, track_id, album_id, date):
        self.name = track_name
        self.id = track_id
        self.album = album_id
        self.date = date

    # a method for printing data members
    def print(self):
        print(self.name)

    
    # method for before and after dates
    def before(self, dates):
        
        for _date in dates:
            print(_date)

    def after(self, dates):
        
        for _date in dates:
            print(_date)


class Date:

    def __init__(self, date):
        self.date = date
        


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
        

def get_all_songs():

    with open('deadmau5_tracks.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        # list to hold song objects
        tracks = []

        # counter
        count = 0

        # bool to skip first line
        first_line = True

        for song in reader:

            # skip first line with metadata info
            if not first_line:

                title = song[0]
                id = song[1]
                album_id = song[2]

                # save data in song object
                song = Song(title, id, album_id, "")
                tracks.append(song)

            # change value of bool
            first_line = False 

    csvfile.close() 

    return tracks


def get_all_albums():

    with open('deadmau5_albums.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"') 

        # list that contains all album objects
        catalog = []

        # list contains all song objects
        tracks = get_all_songs()

        # list contains all song objects in album object
        album_tracks = []

        # bool to skip first line
        first_line = True

        for album in reader:

            # skip first line with metadata info
            if not first_line:

                # num of indices to delete
                i = 0

                # clear album_tracks
                album_tracks = []

                title = album[0]
                id = album[1]
                date = album[2]

                # add tracks to album
                for song in tracks:
                    if song.album == id:
                        album_tracks.append(song)
                        i += 1

                    else: 
                        # erase tracks from list
                        while 0 < i:
                            tracks.pop(0)
                            i -= 1

                        break
                        
                # save data in album object
                album = Album(title, id, date, album_tracks)

                catalog.append(album)

            first_line = False

        # for each song, update before and after with date
        for albums in catalog:
            for songs in album.songs:

                release_dates = []

                date = albums.date.split('-')

                year = date[0]
                month = convert_month(date[1])
                day = date[2]

                reformat_date = date[1] + "/" + date[2] + "/" + date[0]

                release_dates.append(reformat_date)
    
    csvfile.close() 

    return catalog


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