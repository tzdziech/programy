import PySimpleGUI as sg

def CBtn(button_key):
    return sg.Button( key = button_key, button_color=('black', 'white'), size=(4, 2), pad=(0,0))

rows = 3
columns = 5
layout = [["-" for y in range(columns)]  for x in range(rows)]
iter = 0
iter2 = 0
while iter < rows:
    while iter2 < columns:
        layout[iter][iter2] =  CBtn("-B"+str(iter)+str(iter2)+"-")
        iter2 +=1
    iter += 1
    iter2 = 0

window = sg.Window('Pole Gry!', layout, font='Courier 12' )

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    #zwraca key kliknietego przycisku
    clicked_key = window[event].key
    ckx = clicked_key[2]
    cky = clicked_key[3]
    print(clicked_key, ckx, cky)