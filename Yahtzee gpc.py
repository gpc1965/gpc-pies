from random import randint
import winsound
import time
from os import system
rolls = 1
controlo = 0
yat = 0
while True:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    dado3 = randint(1, 6)
    dado4 = randint(1, 6)
    dado5 = randint(1, 6)
    
    print("roll",rolls,": ",dado1, dado2, dado3, dado4, dado5)
    
    if (dado1 == dado2 and dado2 == dado3 and dado3 == dado4 and dado4 == dado5):
        yat = yat + 1
        print("
              !  (of",dado1,
              "'s)",
              "\n",
              "it took you",
              rolls,
              " times to get it.","\n","Ods are 1 in =",
              "{:04.0f}".format(1 / (6 / (6 ** 5))),
              "(","{:04.3f}".format(6 / 7776 * 100),
              "%)")
        winsound.Beep(1250, 300)
        print("*" *60)
        
        n = input("Press ENTER to continue; Press n to exit")
        if n == "n":
              break
        
        if rolls == 1 and yat == 2 or rolls > 7775:
            break
        controlo = controlo + 1
        rolls = 0
        
    rolls = rolls + 1

print("© GPC™ - 2016")
