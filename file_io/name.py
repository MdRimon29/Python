# name = input("Whats your name? ")

names=[]

for i in range(5):
    name = input("Whats your name? ")
    file = open("file_io/names.txt", "a")
    file.write(f"{name}\n")
    file.close()