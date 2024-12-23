print("Modules Demo Initialised")

def factorial(num):
    if num < 0:
        return None
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num+1):
            factorial = factorial * i
        return factorial


if __name__ == '__main__':
    import sys
    print(factorial(int(sys.argv[1])))