# name = input("Whats your name? ")

names=[]

for i in range(3):
    name = input("Whats your name? ")
    
    with open("file_io/names.txt", "a") as file:
        file.write(f"{name}\n")