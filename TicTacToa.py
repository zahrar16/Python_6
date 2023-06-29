
import pyfiglet
import colorama
from colorama import Fore
import time
import random

zaman_shoro = time.time()

def show ():
    for row in tictactoa:
        for col in row:
            if col == "X":
                print(colorama.Fore.RED+col,colorama.Fore.RESET,end="")
            elif col== "0":
                print(colorama.Fore.BLUE+col,colorama.Fore.RESET,end="")
            else:
                print (col,end=" ")
        print()        

def check_game():
    count = 0
    if tictactoa[0][0] == "X" and tictactoa[0][1] == "X" and tictactoa[0][2] == "X" or tictactoa[1][0] == "X" and tictactoa[1][1] == "X" and tictactoa[1][2] == "X" or tictactoa[2][0] == "X" and tictactoa[2][1] == "X" and tictactoa[2][2] == "X":
        print("horra karbar 1 barande shod")
        mohasebe_time()
    if tictactoa[0][0] == "X" and tictactoa[1][0] == "X" and tictactoa[2][0] == "X" or tictactoa[0][1] == "X" and tictactoa[1][1] == "X" and tictactoa[2][1] == "X" or tictactoa[0][2] == "X" and tictactoa[1][2] == "X" and tictactoa[2][2] == "X":        
        print("horra karbar 1 barande shod")
        mohasebe_time()
    if tictactoa[0][0] == "X" and tictactoa[1][1] == "X" and tictactoa[2][2] == "X" or tictactoa[0][2] == "X" and tictactoa[1][1] == "X" and tictactoa[2][0] == "X" :        
        print("horra karbar 1 barande shod")
        mohasebe_time()
    if tictactoa[0][0] == "0" and tictactoa[0][1] == "0" and tictactoa[0][2] == "0" or tictactoa[1][0] == "0" and tictactoa[1][1] == "0" and tictactoa[1][2] == "0" or tictactoa[2][0] == "0" and tictactoa[2][1] == "0" and tictactoa[2][2] == "0":
        print("horra karbar 2 barande shod")
        mohasebe_time()
    if tictactoa[0][0] == "0" and tictactoa[1][0] == "0" and tictactoa[2][0] == "0" or tictactoa[0][1] == "0" and tictactoa[1][1] == "0" and tictactoa[2][1] == "0" or tictactoa[0][2] == "0" and tictactoa[1][2] == "0" and tictactoa[2][2] == "0":        
        print("horra karbar 2 barande shod")
        mohasebe_time()
    if tictactoa[0][0] == "0" and tictactoa[1][1] == "0" and tictactoa[2][2] == "0" or tictactoa[0][2] == "0" and tictactoa[1][1] == "0" and tictactoa[2][0] == "0" :        
        print("horra karbar 2 barande shod")   
        mohasebe_time()
    for row in range(3):
        for col in range(3):    
            if tictactoa[row][col] != "-":
                        count = count + 1
                        if count == 9:
                            print(" DRAW! ")
                            exit()
            
def mohasebe_time():
    zaman_payan = time.time()
    sum = zaman_payan - zaman_shoro
    h=sum//3600
    b=sum-3600*h
    b2 = b // 1
    d=b//60
    print(Fore.GREEN)
    print("Hour:",h,"Minute:",d,"second:",b2)
    print(Fore.RESET)
    exit()
             

text = pyfiglet.figlet_format("Tic Tac Toa", font="slant")
print(text)


tictactoa = [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"]]
show()     

print(Fore.GREEN)
print("PLAYER VS CPU ==> 1 ")
print("PLAYER VS PLAYER ==> 2 ")
print(Fore.RESET)

menu = int(input("enter your choice: "))

if menu == 2:
    show()
    while True:
        print("Plear 1: ")

        while True:
            row = int(input("enter row: "))    
            col = int(input("enter col: "))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if tictactoa[row][col] == "-":   
                    print(colorama.Fore.RED)
                    tictactoa[row][col] = "X" 
                    print(colorama.Fore.RESET)
                    break
                else:
                    print("adda tekrari vard nakon! ")   
            else:
                print("adda 0 or 1 or 2 vared kon")    
                
            
        show()
        check_game()
        print("Plear 2: ")
        while True:
            row = int(input("enter row: "))
            col = int(input("enter col: "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if tictactoa[row][col] == "-":
                    tictactoa[row][col] = "0"
                    break
                else:
                    print("adda tekrari vard nakon! ")
            else:
                print("adda 0 or 1 or 2 vared kon")              
        show()
        check_game()

elif menu == 1:
    show()
    while True:
        print("Plear 1")

        while True:
            row = int(input("enter row: "))    
            col = int(input("enter col: "))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if tictactoa[row][col] == "-":   
                    tictactoa[row][col] =  "X"
                    break
                    
                else:
                    print("adda tekrari vard nakon! ")   
            else:
                print("adda 0 or 1 or 2 vared kon")    
        show()
        check_game()
       
        print("Plear2 : ")
        while True:
            
            row = random.randint(0,2)
            print(row)
            col = random.randint(0,2)
            print(col)
            if 0 <= row <= 2 and 0 <= col <= 2:
                if tictactoa[row][col] == "-":
                    tictactoa[row][col] = "0"
                    break
                else:
                    print("adda tekrari vard nakon! ")
            else:
                print("adda 0 or 1 or 2 vared kon")              
        show()
        check_game()
