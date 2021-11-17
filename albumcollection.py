"""..."""
import csv

import pandas as pd

from album import Album


class AlbumCollection:
    albums = []
    def __init__(self, albumslist= []):
        self.albums = albumslist

    def load_albums(self, filename):
        if len(open(filename).readlines())==1:
            print('文件为空！')
        else:
            with open(filename, 'rt', ) as csvfile:
                reader = csv.reader(csvfile)
                for rows in enumerate(reader):
                    if rows[1][0] == 'title':
                        continue
                    new_album = Album(rows[1][0], rows[1][1], rows[1][2], (True,False)[rows[1][3]=='r'])
                    self.albums.append(new_album)

    def sort(self):
        res = sorted(self.albums, key=lambda s: s.artist)
        print('按艺术家排序后：')
        for i in range(len(res)):
            print(res[i].title+',', res[i].artist+',', res[i].year+',', ('r', 'c')[res[i].is_completed])

    def add_album(self, album):
        album.__add__('albums.csv')
        print('添加成功后：')
        Album.show_all()


