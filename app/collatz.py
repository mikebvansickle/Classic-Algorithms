def step(n):
    if n%2 == 1:
        return n*3 + 1
    else:
        return n/2

def collatz(n):
    count = 0
    if n < 1:
        return 0
    while n != 1:
        n = step(n)
        count += 1
    return count
