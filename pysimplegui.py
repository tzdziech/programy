import PySimpleGUI as psg

layout = [
	[psg.Button("Przycisk", key = "-BUTTON1-"), psg.Text()],
	[psg.InputText(key = "-INPUT-")]
]

psg.Text
window = psg.Window("oKNo", layout)

while True:
    # .read dopiero powoduje ze okno sie pojawia
	event, values = window.read() 
		
		# event zwraca akcje jakie sa w oknie
		# to na zamkniecie
	if event == psg.WIN_CLOSED:
		break
		
	if event == "-BUTTON1-":
		print("nacisniecie przycisku itd")
		print(values)
		print("dupa")
		string = values
		psg.Popup("Zegnaj, będzie nam smutno", string)
		break
        

# to oczywiscie zamyka okno
window.close() 


