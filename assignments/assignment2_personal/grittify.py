#!/usr/bin/env python
import csv
from datetime import datetime
from sys import argv
# from music import Album, Song
import calendar

class Album: 
  
    # default constructor 
    def __init__(self, album): 
        self.album = album
  
    # a method for printing data members 
    def print(self): 
        print(self.album) 


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
        

def get_all_albums2():

    # reads the file 
    f = open('deadmau5_albums.csv', 'r')

    #  list to store albums
    albums = []

    # counter
    count = 0

    # print(f.read())
    for line in f.readlines():
        
        # skip the first line of file
        if count > 0:

            # delete \n characters
            line = line.replace('\n', '')

            # turn each line into an array
            line_array = line.split(',')

            # reformat date
            date = line_array[2].split('-')

            year = date[0]
            month = date[1]
            day = date[2]

            # convert num of month to name of month
            month = convert_month(month)

            print(month)

            # info for each animal is stored in a dict
            obj = Album(line_array[0] + " by deadmau5, released on " + month
            + ' ' + day + ' ' + year)

            # add each dict to animals list
            albums.append(obj)

        count = count + 1

        # close the file
        f.close()

    return albums


def get_all_albums():

    albums = []

    with open('deadmau5_albums.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"') 

        i = 0

        for album in reader:

            date = album[2].split('-')
            

            # # convert num of month to name of month
            # month = convert_month(month)

            # print(month)

            # info for each animal is stored in a dict
            album = Album(album[0] + " by deadmau5, released on ")


            albums.append(album)

            

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