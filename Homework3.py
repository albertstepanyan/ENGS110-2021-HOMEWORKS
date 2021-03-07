def Prime_Check (Number):
    count = 0
    i = 2

    while(i <= Number//2):
        count = count + 1
        break
    i = i + 1

    if (count == 0 and Number != 1):
        print("%d is a prime number" %Number)
        return Number
    else:
        print("%d is not a prime number" %Number)
        return False

def main():

    Number = int(input( " Please enter any number: "))
    Prime_Check(Number)


    F1 = 0
    F2 = 1
    Sum = 0
    F3 = 0
    while F3 + F1 < Number :
        F3 = F1 + F2
        Sum = Sum + F3
        F1 = F2
        F2 = F3


    if (1 <= Sum):
        Final_Sum = bin(Sum + 1)[2 : ]
        print("Final sum is %s" %Final_Sum)
    else:
        print("Sorry wrong input")


main()
