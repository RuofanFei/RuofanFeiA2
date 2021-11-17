"""..."""
import csv
import pandas as pd

class Album:

    def __init__(self, title="", artist="", year=0, completed=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_completed = completed

    @staticmethod
    def show_all():
        print('here is the list of albums')
        data = pd.read_csv('albums.csv')
        print(data)

    def __add__(self, filename):
        with open(filename, 'a', encoding='utf-8', newline='')as f:
            writer = csv.writer(f)
            writer.writerow([self.title, self.artist, self.year, ('r', 'c')[self.is_completed]])
        print("add successfully")

    def mark_completed(self):
        self.is_completed= True
        with open('albums.csv', 'rt') as csvfile:
            reader = csv.reader(csvfile)
            for rows in enumerate(reader):
                if rows[1][0] == self.title:
                    row = rows
        df = pd.read_csv('albums.csv')
        s = df.drop(row[0]-1)
        s.to_csv('albums.csv', index=False)
        row[1][3] = 'c'
        with open('albums.csv', 'a', encoding='utf-8', newline='')as f:
            writer = csv.writer(f)
            writer.writerow(row[1])
            print("修改成功")






