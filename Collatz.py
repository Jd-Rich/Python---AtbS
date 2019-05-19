def collatz(num):
    #determine if odd or even
    if num % 2 == 0:
        #num is even
        print(num // 2)
        return(num //2)
    else:
        #num is odd
        print(num * 3 + 1)
        return(num * 3 + 1)


goodInput = False

while goodInput == False:
    try:
        num = int(input("Enter a number"))
        goodInput = True
    except ValueError:
        print("You need to enter a numerical value.")

while num != 1:
    num = collatz(num)