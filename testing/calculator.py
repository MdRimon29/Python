def main():
    n = int(input("Enter a number: "))
    print("n square is: ", Square(n))
    
def Square(n):
    return n**2
    
if __name__ == "__main__":
    main()