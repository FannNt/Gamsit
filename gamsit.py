import random

player = ["G","M","S"]
computer1 = ["G","M","S"]

def com1():
    mCom = random.choice(player)

    if mCom in player:
        player.remove(mCom)
        print(f"Computer memilih {mCom}")
        print(f"Sisa jari anda {player}")
        print(f"Sisa jari Computer {computer1}")
    

def p1():
    print(computer1)
    match1 = input("Pilih apa yang akan ada hilangkan!: ").upper()
    if match1 in computer1:
        computer1.remove(match1)
        com1()
    else:
        print("Masukkan dengan benar")
        p1()
def p2():
    print(" ")
    print(computer1)
    match2 = input("Pilih apa yang akan ada hilangkan!: ").upper()
    if match2 in computer1:
        computer1.remove(match2)
        com1()
    else:
        print("Masukkan dengan benar")
        p2()
def mk():
    if (player == ["S"] and computer1 == ["G"]) or (player == ["G"] and computer1 == ["M"]) or (player == ["M"] and computer1 == ["S"]):
        print(f"\nKamu menang \nComputer = {computer1}\nPlayer = {player}")
    elif player == computer1:
        print(f"\nSeri \nComputer = {computer1}\nPlayer = {player}")
    else:
        print(f"\nNT\nComputer = {computer1}\nPlayer = {player}")

def play():
    p1()
    p2()
    mk()

play()

while True:     
    loop = input("Apakah mau lanjut ? y/n : ").upper()
    if loop == "Y":
        player = ["G","M","S"]
        computer1 = ["G","M","S"]
        play()
    elif loop == "N":
        break
    else:
        print("Masukkan Y/N!!!!!")
        pass

        