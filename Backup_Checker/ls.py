import glob
import os
import datetime
from pickle import FALSE
import numpy as np

#zwraca numer pozycji najwiekszego pliku z listy o zadanym rozszezeniu
def find_biggest(list, extension):
    last_biggest = list[2,0]
    number_biggest = FALSE
    for x in range(len(list[0])):
        if list[2,x] > last_biggest and list[3,x] == extension:
            last_biggest = list[2,x]
            number_biggest = x

    print("Najwiekszy plik to:", list[0,number_biggest], list[1,number_biggest])
    return number_biggest

#zwraca numer pozycji najnowszego pliku z listy o zadanym rozszezeniu
def find_newest(list, extension):
    last_newest = list[4,0]
    number_newest = FALSE
    for x in range(len(list[0])):
        if list[4,x] > last_newest and list[3,x] == extension:
            last_newest = list[4,x]
            number_newest = x

    print("Najnowszy plik to:", list[0,number_newest], list[1,number_newest])
    return number_newest

#konwersja rozmiaru na jak najwieksze jednostki
def convert_bytes(size):
    """ Convert bytes to KB, or MB or GB"""
    size = float(size)
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.2f %s" % (size, x)
        size /= 1024.0

#print calej listy
def do_ls(list):
    
    for x in range(len(list[0])):
        print("File name:", list[0,x],"\t size:", list[1,x],"(", list[2,x], ") \textension:", list[3,x], "\t last modified:", list[4,x], "(", datetime.datetime.fromtimestamp(float(list[4,x])), ")")
    print("Znaleziono:", len(list[0]), "pliki")

#wyodrebnienie rozszezenia z nazwy pliku
def get_extension(file):
    file_details = os.path.splitext(file)
    return file_details[1]

#pobranie danych do stworzenia list
path = ""
size = [] #lista z rozmiarami
natural_size = []
file_extension = [] #lista z rozszezeniami
file_modification_time = []
files = glob.glob(path+"*.*")
for file in files:    
    size.append(convert_bytes(os.path.getsize(file)))#pobiera rozmiar i conwertuje na najwieksze jednostki
    natural_size.append(os.path.getsize(file))
    file_extension.append(get_extension(file))    
    file_modification_time.append(os.path.getmtime(file))

#stworzenie tablicy z list
#zadana list plikow:  0 - nazwa, 1- rozmiar zmienony, 2 - rozmiar naturalny, 3 - rozszezenie, 4 - czas) 
ls = np.array([files, size, natural_size, file_extension, file_modification_time])

#pierwsza wartos to kolumna, druga to wierszczyli: 0,0 - nazwa, 1,0 - rozmiar
print(ls[1,0])

do_ls(ls)

find_biggest(ls,".py")
find_newest(ls,".py")



