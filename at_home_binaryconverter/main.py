import numpy as np
def script():
    i = int(input("How many bits are you converting?\n"))
    if i > 8:
        print("This converter only works in bytes, please enter a number under 8")
        script()
    else:
        a = np.arange(i)
        b = a[::-1]
        b1 = 2 ** b
#print(b1)

    binString = input("What is your binary string\n")
    n = binString
    c = [int(d) for d in str(n)]
#print(c)

    bin_conv =np.sum(np.multiply(b1, c))
    print("The decimal conversion of your binary string is ", bin_conv)

    if i == 4:
        if bin_conv == 15:
            print("The hexadecimal conversion of your binary code is f")
            script()
        elif bin_conv == 14:
            print("The hexadecimal conversion of your binary code is e")
            script()
        elif bin_conv == 13:
            print("The hexadecimal conversion of your binary code is d")
            script()
        elif bin_conv == 12:
            print("The hexadecimal conversion of your binary code is c")
            script()
        elif bin_conv == 11:
            print("The hexadecimal conversion of your binary code is b")
            script()
        elif bin_conv == 10:
            print("The hexadecimal conversion of your binary code is a")
            script()
        else:
            print("The hexadecimal conversion of your binary string is ", bin_conv)
            script()
    else:
        script()

script()
