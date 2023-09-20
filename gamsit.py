import random

player = ["G","M","S"]
computer = ["G","M","S"]

def com1():
    Com = random.choice(player)

    if Com in player:
        player.remove(Com)
        print(f"Computer memilih {Com}")
        print(f"Sisa jari anda {player}")
        print(f"Sisa jari Computer {computer}")
    

def match():
    print("-----------------------")
    print(computer)
    match1 = input("Pilih apa yang akan ada hilangkan!: ").upper()
    if match1 in computer:
        computer.remove(match1)
        com1()
    else:
        print("Masukkan dengan benar")
        match()

def nilai():
    if (player == ["S"] and computer == ["G"]) or (player == ["G"] and computer == ["M"]) or (player == ["M"] and computer == ["S"]):
        print(f"\nComputer = {computer}\nPlayer = {player}\nKamu menang")
    elif player == computer:
        print(f"\nComputer = {computer}\nPlayer = {player}\nSeri")
    else:
        print(f"\nComputer = {computer}\nPlayer = {player}\nNT")

def play():
    match()
    match()
    nilai()

play()

while True:     
    loop = input("Apakah mau lanjut ? y/n : ").upper()
    if loop == "Y":
        player = ["G","M","S"]
        computer = ["G","M","S"]
        play()
    elif loop == "N":
        break
    else:
        print("Masukkan Y/N!!!!!")
        pass

        