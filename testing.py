def iterative_factorial(n):
    factorial = 1
    if n == 0:
        return factorial
    else:
        for i in range(1,n+1):
            factorial *= i
        return factorial

def recursive_factorial(n):
    if n == 0:
        factorial = 1
    else:
        factorial = n * recursive_factorial(n-1)
    return factorial

def moveDiscs(num, frmPeg, toPeg, tmpPeg):
    if num > 0:
        moveDiscs(num-1, frmPeg, tmpPeg, toPeg)
        print(f"Move a disc from peg {frmPeg} to peg {toPeg}")
        moveDiscs(num-1, tmpPeg, toPeg, frmPeg)

if __name__ == '__main__':
    number = 3
    # print(iterative_factorial(number))
    # print(recursive_factorial(number))
    moveDiscs(number, 1, 3, 2)