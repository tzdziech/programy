from asyncio import exceptions
from logging import exception
from math import ceil
from msilib.schema import Property
from tkinter import EXCEPTION

#jak nazywac wyjatki po swojemu? - w nawiasie Exception bo dziedziczyc ma po classie Exception
class InvalidSemester(Exception):
    pass


#class Student
class Student:
    #konstruktor - z jakimi danymi bedzie tworzony
    def __init__(self, first_name, last_name):
        #self czyli this - wskzauje na obiekt w ktorym sie znajdujemy / na ktorym metoda jest wywolywana
        self.first_name = first_name
        self.last_name = last_name
        self.semestr = 5

    # dekorator @property - powoduje ze ponizsdzej funkcji mozemy uzyc bez () czyli np self.year 
    #jako zmienna zwroci wartoc a nie funkcjia
    @property
    def year(self): 
        return ceil(self.semestr / 2)
    
    #metoda - czyli funkcja w klasie, musi miec SELF
    def hello(self):
        return f'Man na imie {self.first_name}, a na nazwisko {self.last_name} studiuje na {self.year} roku'

    def go_up(self):
        self.semestr += 1

    def go_down(self):
        #wyjatek, jak cos sie spieroli w tym przypadku semestr mniejszy od jeden
        if self.semestr <= 1:
            raise InvalidSemester("Nie mozesz bardziej obnizyc semestru")

        self.semestr -= 1

    

        

    
    # pass - to piszemy jesli pusta
    
#z obsluga wyjatkow
try:
    tomek = Student(first_name="Tomek", last_name="Zdziech")
    #print("Obiekt", tomek)
    #print("Imie", tomek.first_name)
    tomek.go_down()
    print(tomek.hello())
    tomek.go_down()
    tomek.go_down()
    tomek.go_down()
    tomek.go_down()
    print(tomek.hello())
    tomek.go_down()
except InvalidSemester as message:
    print(message)