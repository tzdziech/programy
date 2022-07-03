



from time import time


def ifis_Pierwsza(number1):
    iter = 2
    while iter < number1:
        if number1%iter == 0:
            return False
        iter += 1

    return True
   



number = int(input("Podaj liczbe do ktorej liczymy: "))
suma_pierwszych = 0

licznik = 2
czas = time()
while licznik < number:
    if ifis_Pierwsza(licznik):
        #suma_pierwszych += 1
        print(licznik, "- to liczba pierwsza, znalezionych liczb pierwszych:")
    licznik += 1
print("Uplynelo czasu:", time()-czas)