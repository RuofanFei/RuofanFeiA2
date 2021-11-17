"""..."""
# Copy your first assignment to this file, then update it to use the Album class

from album import Album
"""Update this module docstring with your own details
Name:RuofanFei
Date started:2021/10/1
"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
from album import Album


def menu():
    print("menu:")
    print("L-list all albums")
    print("A-add new album")
    print("M-mark an album as completed")
    print("Q-quit")


def show_all():
    Album.show_all()


def add():
    a = input("the album's name")
    b = input("the singer's name")
    c = input("Album release year")

    new_album = Album(a, b, c, False)
    new_album.__add__('albums.csv')


def mark():
    a = int(input("choose the title you wannna change:"))
    new_album = Album(a, " ", 0, False)
    new_album.mark_completed()
    show_all()


def set_file():
    header = ['name', 'singer', 'year', 'completed']
    rows = [('The Dark Side of the Moon', 'Pink Floyd', '1973', 'r'),
            ('Common Jasmin Orange', 'Jay Chou', '2004', 'r'),
            ('After the Music Stops', 'Lecrae', '2019', 'c'),
            ('Honey', 'Lay', '2019', 'c')]

    with open('albums.csv', 'w', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def main():
    set_file()
    menu()
    a = 1
    while a != 'Q':
        a = input()
        if a == 'L':
            show_all()
        elif a == 'A':
            add()
        elif a == 'M':
            mark()
        elif a == 'Q':
            print()
        else:
            print("input wrong")
    print("thank use")


main()

