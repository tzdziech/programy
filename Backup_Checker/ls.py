from pip import main
from tkinter import *
import FileList as fl
from tkinter import ttk
import glob
import tomli


if __name__ == '__main__':
    main_list = fl.FileList("") #jesli folder sieciowy to podwoje backslashe \\\\Desktop-sj7tn1k\\wii\\
    #print(main_list.list)
    #main_list.do_ls()
    #main_list.find_biggest(".py")
    #main_list.find_newest(".py")

    mainWindow = Tk()

    def StartButton():
        temp_file = fileListComboBOx.get() #pobiera z widgetu wybrana wartosc
        
        #wgranie pliku .toml
        fp = open(temp_file, mode="rb")
        toml = tomli.load(fp)
        print(toml)

        mainText.insert(END, toml ) #wypluwa do pola tekstowego


    #inicjacja glownego okna
    mainWindow.geometry("420x420")
    mainWindow.title("Backup Checker - by Tomasz") 
    mainWindow.config(background="GREY") 
    icon = PhotoImage(file='icon.png')
    mainWindow.iconphoto(True, icon) 

    #elementy okna definicje
    fileListComboBOx = ttk.Combobox(mainWindow, values = glob.glob("config\*.*"))    
    fileListComboBOx.set("Wybierz")
    startButton = Button(mainWindow, text="Start", command = StartButton)
    mainText = Text(mainWindow, height = 300, width = 300)

    #elemty okna inicjacja
    fileListComboBOx.pack()
    startButton.pack()
    mainText.pack()

    

    #text_field.insert(END, main_list.find_biggest(".py") )
    #text_field.insert(END, main_list.find_newest(".py") )

   

    mainWindow.mainloop()
  