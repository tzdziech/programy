import os


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"] 

def check_victory():
  players = ["X", "O"]
  for player in players:
    #poziomy
    if board[0] == player and board[1] == player and board[2] == player:
      return player
    if board[3] == player and board[4] == player and board[5] == player:
      return player
    if board[6] == player and board[7] == player and board[8] == player:
      return player    
    #piony
    if board[0] == player and board[3] == player and board[6] == player:
      return player
    if board[1] == player and board[4] == player and board[7] == player:
      return player
    if board[2] == player and board[5] == player and board[8] == player:
      return player
    #przekatne
    if board[0] == player and board[4] == player and board[8] == player:
      return player
    if board[2] == player and board[4] == player and board[6] == player:
      return player
  return "-"

def display_board():
  print(board[0],"|",board[1],"|",board[2], "  0|1|2")
  print("---------")
  print(board[3],"|",board[4],"|",board[5], "  3|4|5")
  print("---------")
  print(board[6],"|",board[7],"|",board[8], "  6|7|8")

#wyswietl mozliwe wybory
def print_possible():
  iter = 0
  print("Pola mozliwe do wybrania:", end = "")
  while iter < 9:
    if board[iter] == "-":
      print(iter, " ", end = "")
    iter+=1
  print("")

def check_possible(number):
  if board[number] == "-":
    return True
  else:
    print("Pole już zajęte")
    return False


def check_range(number):
  if number < 0 or number > 8 :
    print("Wybór spoza dostepnego zakresu")
    return False
  #print("liczba w przedziale prwidlowym", number)
  return True

  
def player_turn(znak):
  print_possible()
  while True:
    wybor = int(input("Wybierz: "))
    if check_range(wybor) == False:
      continue
      
    if check_possible(wybor): 
      print("Wybrales pole:", wybor)
      board[wybor] = znak
      break
    else:
      continue
  

def clean_screen():
  clear = lambda: os.system('cls')
  clear()

def get_winner():
  winner = "-"
  winner=check_victory()
  if winner == "X" or winner == "O":
      print("Zwyciezca to", winner)
      return True
  else:
    return False
  
def change_player(sign):
    if sign == "X":
        return "O"
    elif sign == "O":
        return "X"
    else:
        printf("ZNAK NIEZNANY")


def play():
  
  player_sign = "X"
  clean_screen()
  display_board()
  while True:  
    player_turn(player_sign)
    clean_screen()
    display_board()
    player_sign = change_player(player_sign)
    if get_winner():
      break
    

play()