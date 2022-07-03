#komentarz
from random import randrange
import random

leap = False
year = 400

if year%4 == 0:
    leap = True
    print("Przez 4")
if year%100 == 0:
    leap = False
    print("Przez 100")
if year%400 == 0:
    leap == True
    print("Przez 400")

print(year, leap)

