number = int(input("Enter a widht/hight: "))
symbol = input("Enter something: ")

for i in range(0, number):
    for x in range(0, number):
        if x == number - 1:
            print(symbol, end="\n")
        else:
            print(symbol, end=" ")
