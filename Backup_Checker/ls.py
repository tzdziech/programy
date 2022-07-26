from sys import path
from tkinter.tix import DirList
from pip import main
from tkinter import *
import FileList as fl
from tkinter import ttk
import glob
import tomli
import os
import shutil
from datetime import datetime, date
import time

"""
Format raportów:
Veeam B&R
Data	Wykonujący 	Status	Oryginalny rozmiar maszyny [TB]	
Data ostatniego pełnego backupu 	Rozmiar backupu [GB]	
Data ostatniego wykonanego backupu	Wolne miejsce w repozytorium [GB]	Uwagi

SQL
Data	Wykonujący kontrolę	Status	Rozmiar pliku BAK	Data ostatniego backupu 	
Wolne miejsce w repozytorium 	Uwagi


"""


if __name__ == '__main__':

    sqlExtension = ".bak"
    veaamExtension = "vrb" # do sprawdzenia czy kazdy ma to rozszezenie
    veeamFullExtension = ".vbk" #pelny


    main_list = fl.FileList("") #jesli folder sieciowy to podwoje backslashe \\\\Desktop-sj7tn1k\\wii\\
    #print(main_list.list)
    #main_list.do_ls()
    #main_list.find_biggest(".py")
    #main_list.find_newest(".py")

    mainWindow = Tk()

    """
        kroki: (ju po wczytaniu pliku konfiguracyjnego)
        - odczytuje katalogi
        iF SQL
            w kazdym katalogu:
            ostatni plik na jego podstawie wyplówa tekst do wklejenia
            jesli plki starszy niz dwa dni WARNING!!!

            !!!!! co jesli sa w jednym folderze???????? czy brak dla Express???

        ELIF VEEAM
            w kazdym katalogu:
            1. wyszukuje ostatni backup
            2. wyszukuje ostatni pelny backup
            zaleznie od tego ktory jest najmlodszy generujemy linie do wklejenia
            jesli plki starszy niz dwa dni WARNING!!!
        
        """
    def get_free_space_string(path: str):
        total, used, free = shutil.disk_usage(path)
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if total < 1024.0:
                break
            free /= 1024.0
            total /= 1024.0
            unit = x
        return "%3.2f" % free + x + " / " + "%3.2f" % total + x 
        #moze by tak zwroci jeszcze procent albo ostrzegac gdy miejsce jest mniejsze niz backup???


    #zwraca liste foderow w folderze nadrzednym
    def get_directories(path: str) -> list[str]:
        dirList = []
        p=os.listdir(path)
        for i in p:
            if os.path.isdir(path+i):                
                dirList.append(path+i+"\\")
        return dirList

    #przeszukanie folderu podrzednego
    def sub_folder_execute(path: str, type: str) -> None:
        #print("-------",path,"-------------------")
        fileList = fl.FileList(path)
        #fileList.do_ls()
        if type == "SQL":
            #Data	
            day = date.today()
            print(day.strftime("%d.%m.%Y"), end = "	")
            #Wykonujący kontrolę	
            print("Tomasz Zdziech", end = "	")
            #Status	
            print("ok", end = "	")
            #Rozmiar pliku BAK (nazwa)	oraz Data ostatniego backupu
            file_info = fileList.find_newest(sqlExtension)
            file_day = time.strftime("%d.%m.%Y %H:%M", time.localtime(float(file_info['date'])))
            #print(file_day)
            if file_info :
                print(file_info['size'],"(", file_info['file'],")	", file_day, end = "	")
                #datetime.fromtimestamp(float(file_info['date']))
            #Wolne miejsce w repozytorium 
            print(get_free_space_string(path))
            #Uwagi
            """
            Potencjalnie mozna tu sprawdzac:
            - czy nie ma miejsca malo (porownujac do rozmiaru pliku backupu)
            - czy backup nei jest starszy niz ILEŚ dni
            - czy wogole znaleziono PLIKI!!!

            """


            #print(fileList.find_biggest(sqlExtension), end = "	")
            #print(fileList.find_newest(sqlExtension))
        elif type == "VEEAM":
            print(fileList.find_biggest(veaamExtension))
            print(fileList.find_newest(veaamExtension))
            print(fileList.find_biggest(veeamFullExtension))
            print(fileList.find_newest(veeamFullExtension))
        
        
        
        


    #odpalamy sie w folderze podanym w TOML
    def main_folder_execute(toml):      
        
        if toml['sql'] == "yes":
            print("Szukamy backupow SQL")
            print("Klient", toml['company'])
            print("Data	Wykonujący kontrolę	Status	Rozmiar pliku BAK	Data ostatniego backupu 	Wolne miejsce w repozytorium 	Uwagi")
            dirList = get_directories(toml["path"])
            for i in dirList:
                sub_folder_execute(i, "SQL")

        if toml['veeam'] == "yes":
            print("Szukamy backupow VEEAM")
            dirList = get_directories(toml["path"])
            for i in dirList:
                sub_folder_execute(i, "VEEAM")

        #print(dirList)



    def start_button():
        temp_file = fileListComboBOx.get() #pobiera z widgetu wybrana wartosc
        
        #wgranie pliku .toml
        fp = open(temp_file, mode="rb")
        toml = tomli.load(fp)

        main_folder_execute(toml)
        
        
        #print(toml)
        mainText.delete("1.0", "end")
        mainText.insert(END, toml ) #wypluwa do pola tekstowego
        mainText.insert(END, '\n')
        mainText.insert(END, toml['company']+'\n')
        mainText.insert(END, toml['path']+'\n')


    #inicjacja glownego okna
    mainWindow.geometry("420x420")
    mainWindow.title("Backup Checker - by Tomasz") 
    mainWindow.config(background="GREY") 
    icon = PhotoImage(file='icon.png')
    mainWindow.iconphoto(True, icon) 

    #elementy okna definicje
    fileListComboBOx = ttk.Combobox(mainWindow, values = glob.glob("config\*.*"))    
    fileListComboBOx.set("Wybierz")
    startButton = Button(mainWindow, text="Start", command = start_button)
    mainText = Text(mainWindow, height = 300, width = 300)

    #elemty okna inicjacja
    fileListComboBOx.pack()
    startButton.pack()
    mainText.pack()

   



    #text_field.insert(END, main_list.find_biggest(".py") )
    #text_field.insert(END, main_list.find_newest(".py") )

   

    mainWindow.mainloop()
  
  