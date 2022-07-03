# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def is_valid(letter):
    
    if letter == "0":
            return True
    if letter == "1":
            return True
    if letter == "2":
            return True
    if letter == "3":
            return True
    if letter == "4":
            return True
    if letter == "5":
            return True
    if letter == "6":
            return True
    if letter == "7":
            return True
    if letter == "8":
            return True
    if letter == "9":
            return True
    if letter == "a" or letter == "A":
            return True
    if letter == "b" or letter == "B":
            return True
    if letter == "c" or letter == "C":
            return True
    if letter == "d" or letter == "D":
            return True
    if letter == "e" or letter == "E":
            return True
    if letter == "f" or letter == "F":
            return True

    return False


def is_hash(letter):

    if letter == "#":
        return True
    else:
        return False


def lenght_ok(string):

    if len(string) == 4 or len(string) == 7:
        return True
    else:
        return False


wynik = ""
ciag = sys.stdin   
znacznik = False
start = False

for linia in ciag:
    for litera in linia:
        #print(wynik)
        #znalezlismy hash teraz zczytujemy znaki
        
        if litera == "{": 
            start = True
        elif litera == "}":
            start = False
        
        if znacznik==True:
            if is_valid(litera):
                wynik+=litera
            # print("dobry znak")
            else:
                #print("zly znak")
                if lenght_ok(wynik):
                    print(wynik)
                    wynik = ""
                    znacznik = False
                else:
                    wynik = ""
                    znacznik = False
                # print("zla dlugosc - reset")
                    continue

        #znajdujemy hash
        if is_hash(litera) and start == True:
            znacznik = True
            wynik+=litera
            #print("mam hash")
            continue