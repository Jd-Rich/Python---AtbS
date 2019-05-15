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

num = int(input("Enter a number"))

while num != 1:
    num = collatz(num)