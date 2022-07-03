from random import randint, random
import time
import keyboard
import os
import PySimpleGUI as sg

ghostFile ="C:\\Users\\Agron\\Documents\\NAUKA\\PYTHON\\programy\\LABIRYNT\\duszek.png"
treasureFile = "C:\\Users\\Agron\\Documents\\NAUKA\\PYTHON\\programy\\LABIRYNT\\skarb.png"
playerFile = "C:\\Users\\Agron\\Documents\\NAUKA\\PYTHON\\programy\\LABIRYNT\\pacman.png"
emptyFile = "C:\\Users\\Agron\\Documents\\NAUKA\\PYTHON\\programy\\LABIRYNT\\puste.png"
crossFile  = "C:\\Users\\Agron\\Documents\\NAUKA\\PYTHON\\programy\\LABIRYNT\\cross.png"

def CBtn(button_key, buttonText):

    imageSource = False
    if(buttonText == "D"):
        imageSource = ghostFile
    elif(buttonText == "X"):
        imageSource = treasureFile
    elif(buttonText == "@"):
        imageSource = playerFile
    elif(buttonText == "-"):
        imageSource = crossFile
    elif(buttonText == " "):
        imageSource = emptyFile

        #sg.Image()

    return sg.Image( key = button_key,  source = imageSource, pad = (0,0))



rows = 5
columns = 5

#inicjacja layoutu
layout = [["-" for y in range(columns)]  for x in range(rows)]

#X jest w pionie = rows, Y w poziomie = columns
#player position pp
pp_x = 0 
pp_y = 0 

#goal position gp 
gp_x = 0 
gp_y = 0

#pole pod graczem
ppg = "-"

#ilosc ruchow
moves_count = 0

#duszki
ghosts_number = 1
ghosts = [["0" for y in range(2)] for x in range(ghosts_number)]

# y - ilosc kolumn , x ilosc wierszy
matrix = [["-" for y in range(columns)]  for x in range(rows)] 

def generate_layout():
    global layout

    iter = 0
    iter2 = 0
    while iter < rows:
        while iter2 < columns:
            layout[iter][iter2] =  CBtn("-B"+str(iter)+str(iter2)+"-", matrix[iter][iter2])
            iter2 +=1
        iter += 1
        iter2 = 0
    #layout = layout + [[CBtn("w"),CBtn("d"),CBtn("s"),CBtn("a")]]

def empty_matrix():
    x = 0
    y = 0
    while x < rows:
        while y < columns:
            matrix[x][y] = "-"
            y += 1
        #print()
        x+=1
        y=0

def clean_screen():
  clear = lambda: os.system('cls')
  clear()

def show_area():
    x = 0
    y = 0
    
    while x < rows:
        while y < columns:
            print(matrix[x][y], end = "")
            y += 1
        print()
        x+=1
        y=0

def randomise_holes():
    global matrix, rows, columns
    maks = randint(10,20)
    iter = 0
    #print("maks",maks)
    while iter < maks:
        #print("iter",iter)
        matrix[randint(0,rows-1)][randint(0,columns-1)] = " "
        iter += 1

def initiate_positions():
    global pp_x, pp_y, gp_x, gp_y, rows, columns
    #print(matrix)
    pp_x = randint(0,rows-1)
    pp_y = randint(0,columns-1)
    #print("Player", pp_x, pp_y)
    gp_x = randint(0,rows-1)
    gp_y = randint(0,columns-1)

    matrix[pp_x][pp_y] = "@"
    matrix[gp_x][gp_y] = "X"

def check_edges(direction):
    if direction == "a":
        if pp_y - 1 < 0:
            return False
        else:
            return True
    elif direction == "d":
        if pp_y + 1 > columns - 1:
            return False
        else:
            return True
    elif direction == "w":
        if pp_x -1 < 0:
            return False
        else:
            return True
    elif direction == "s":
        if pp_x + 1 > rows - 1:
            return False
        else:
            return True

def move(direction):
    global pp_x, pp_y, gp_x, gp_y, matrix, ppg, moves_count
    if direction == "a":
        matrix[pp_x][pp_y] = "-"
        pp_y -= 1
        ppg = matrix[pp_x][pp_y]
        matrix[pp_x][pp_y] = "@"
    elif direction == "d":
        matrix[pp_x][pp_y] = "-"
        pp_y += 1
        ppg = matrix[pp_x][pp_y]
        matrix[pp_x][pp_y] = "@"
    elif direction == "w":
        matrix[pp_x][pp_y] = "-"
        pp_x -= 1
        ppg = matrix[pp_x][pp_y]
        matrix[pp_x][pp_y] = "@"
    elif direction == "s":
        matrix[pp_x][pp_y] = "-"
        pp_x += 1
        ppg = matrix[pp_x][pp_y]
        matrix[pp_x][pp_y] = "@"
    moves_count += 1


def check_victory_condition():
    if pp_x == gp_x and pp_y == gp_y:
        return "v"
    elif ppg == " ":
        return "h"
    else:
        return "c"

def move_actions_and_checks(direction):
    if check_edges(direction):
        move(direction)
    else:
        print("nie mozna sie tam ruszyc")

def show_info():
    print("> X < to twój cel, ty jesteś oznaczony > @ <, poruszasz sie za pomocą klawiszy WSAD. Uwazaj zeby nie wpasć w dziury >  <")
    print("> D < to DUCH unikaj go bo cie zje")

def create_ghosts():
    global ghosts, ghosts_number, matrix, rows, columns
    iter = 0
    #print(ghosts)
    while iter < ghosts_number:
        x = randint(0, rows -1)
        y = randint(0, columns -1)
        ghosts[iter][0] = x
        ghosts[iter][1] = y
        matrix[x][y] = "D"
        iter += 1
    #print(ghosts)

#def update_button(x, y, fl):
#    global window
#    window['-B'+str(x)+str(y)+"-"].update(fl)

def basicMove(gN, dir):
    global ghosts, matrix

    window['-B'+str(ghosts[gN][0])+str(ghosts[gN][1])+"-"].update(crossFile)
    matrix[ghosts[gN][0]][ghosts[gN][1]]="-"
    # 1-a, 2-d, 3-w, 4-s
    if dir == 1:
        window['-B'+str(ghosts[gN][0])+str(ghosts[gN][1]-1)+"-"].update(ghostFile)
        matrix[ghosts[gN][0]][ghosts[gN][1]-1]="D"
    elif dir == 2:
        window['-B'+str(ghosts[gN][0])+str(ghosts[gN][1]+1)+"-"].update(ghostFile)
        matrix[ghosts[gN][0]][ghosts[gN][1]+1]="D"
    elif dir == 3:
        window['-B'+str(ghosts[gN][0]-1)+str(ghosts[gN][1])+"-"].update(ghostFile)
        matrix[ghosts[gN][0]-1][ghosts[gN][1]]="D"
    elif dir == 4:
        window['-B'+str(ghosts[gN][0]+1)+str(ghosts[gN][1])+"-"].update(ghostFile)
        matrix[ghosts[gN][0]+1][ghosts[gN][1]-1]="D"


    

def dieLava(gN):
    global ghosts_number
    print("Zginal duch numer: ", gN, "Bylo: ", ghosts_number, " zostało", end = "")
    window['-B'+str(ghosts[gN][0])+str(ghosts[gN][1])+"-"].update(crossFile)
    matrix[ghosts[gN][0]][ghosts[gN][1]]="-"
    ghosts.pop(gN)
    #ghosts[gN][1].pop()
    ghosts_number -= 1
    print(ghosts_number)


def move_ghost(x, y):

    #warunki brzegowe
    print("sprawdzamy ruch duszka na:", x, y)
    if x < 0 or y < 0 or x >= rows or y >= columns: return 0

    if(matrix[x][y] == "D"): #inny duszek
        return 0
    elif(matrix[x][y] == "X"): #na skarb nie wchodzimy
        return 0
    elif(matrix[x][y] == "@"): #gracz zabijamy
        return 1
    elif(matrix[x][y] == " "): #ginie w lavie
        return 2
    elif(matrix[x][y] == "-"):
        return 3
    

def random_move_ghost(ghost_number):
    global ghosts, matrix
    print("ruch ducha numer", ghost_number)
    #random 1-5 - 1-a, 2-d, 3-w, 4-s
    dir = randint(1,5)
    action = 0
    if dir == 1:
        action = move_ghost(ghosts[ghost_number][0],ghosts[ghost_number][1]-1)
    elif dir == 2:
        action = move_ghost(ghosts[ghost_number][0],ghosts[ghost_number][1]+1)
    elif dir == 3:
        action = move_ghost(ghosts[ghost_number][0]-1,ghosts[ghost_number][1])
    elif dir == 4:
        action = move_ghost(ghosts[ghost_number][0]+1,ghosts[ghost_number][1])
    elif dir == 5:
        return False

    if action == 0: #nie rusza sie
        return
    elif action == 1: # gracz
        basicMove(ghost_number, dir)
    elif action == 2: #lava, duch ginie
        dieLava(ghost_number)
    elif action == 3: # zwykly ruch
        basicMove(ghost_number, dir)



def ghosts_move():
    global ghosts_number
    print("MAMY DUCHY------------")
    print(ghosts)
    print("----------------")

    iter = 0
    while iter < ghosts_number:
        random_move_ghost(iter)
        iter += 1

def update_layout():
    global window, rows, columns
    iter = 0
    iter1 = 0
    
    print("UPDATE LAYOUT")
    while iter < rows:
        while iter1 < columns:
            numeracja = '-B'+str(iter)+str(iter1)+"-"
            
            imageSource = False
            if(matrix[iter][iter1] == "D"):
                imageSource = ghostFile
            elif(matrix[iter][iter1] == "X"):
                imageSource = treasureFile
            elif(matrix[iter][iter1] == "@"):
                imageSource = playerFile
            elif(matrix[iter][iter1] == "-"):
                imageSource = crossFile
            elif(matrix[iter][iter1] == " "):
                imageSource = emptyFile

            #window[numeracja].source = imageSource
            window[numeracja].update(imageSource)
            

            #window[numeracja].ButtonText =  matrix[iter][iter1]
            #dprint(iter, iter1, numeracja, matrix[iter][iter1], window[numeracja].ButtonText)
            iter1 += 1
            
        iter += 1
        iter1 = 0

#STARTUJEMY
randomise_holes()
create_ghosts()
initiate_positions()



generate_layout()

window = sg.Window('Pole Gry!', layout, font='Courier 12', return_keyboard_events=True, use_default_focus=False )
#update_layout()

while True:
    
    event, values = window.read()
    update_layout()
    #window.refresh()
    #clean_screen()
    show_info()
    show_area()
    
  
    print("Pozycja gracza", pp_x, pp_y, "pole pod graczem:>",ppg,"<")
    print("Wykonałes:", moves_count," ruchów.")

    #obsluga okna    
 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    #costam = window[event]
    #window[event].update(costam)

    if event == "w":
        #print("nacisnales w")
        move_actions_and_checks("w") 
    elif event == "s":
        #print("nacisnales s")
        move_actions_and_checks("s") 
    elif event == "d":
        #print("nacisnales d")
        move_actions_and_checks("d") 
    elif event == "a":
        #print("nacisnales a")
        move_actions_and_checks("a") 
    elif event == "q":
        #print("nacisnales q")
        exit()
    
    update_layout()

    #window.refresh()
    
    #obsluga klawiatury
    #if event == sg.press

  #  match keyboard.read_key():
   #     case "w":
    #        move_actions_and_checks("w")          
     #   case "s":
      #      move_actions_and_checks("s")
       # case "a":
        #    move_actions_and_checks("a")
        #case "d":
        #    move_actions_and_checks("d")
        #case "q":
        #    print("q")
        #    exit()
    #time.sleep(0.2)
    
    #Ghosts turn
    ghosts_move()

    match check_victory_condition():
        case "v":
            print("Dotarłeś do celu!!!")
            exit()
        case "h":
            print("Frajerze wlazles do dziury!!! P R Z E G R A L E S !   !   !")
            exit()
        #case "D":
        #    print("Zjadl cie duch")
        case "c":
            continue
    
