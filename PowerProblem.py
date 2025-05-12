import random

def fast_pow(x, n):
    result = 1
    base = x
    while n > 0:
        if n % 2 == 1:
            result *= base
        base *= base
        n //= 2
    return result

if __name__ == "__main__":
    print("Now displaying PowerProblem.")
    x = random.randint(4, 999)
    n = random.randint(3, 40)
    print(f"{x} to the power {n} is: {fast_pow(x, n)}, comparing to built-in: {pow(x, n)}")