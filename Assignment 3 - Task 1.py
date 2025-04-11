y = int(input("Enter a number: "))


def factorial(y):
    if y < 2:
        return 1
    else:
        return y*(factorial(y-1))


result = factorial(y)
print("The Factorial of " + str(y) + " is " + str(result))
