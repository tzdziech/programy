import keyboard
import time

def show():
  	#show key
    while True:
        key = keyboard.read_key()
        print("poszlo", key)
        #reset show()
        #if keyboard != "":
        print("if")
        time.sleep(0.2)
           # show()

#start
show()