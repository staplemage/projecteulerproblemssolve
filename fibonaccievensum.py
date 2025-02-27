fib = 1
fiblast = 1
count = 0
sumFib = 0

while (fib < 4000000):
    fib += fiblast
    if (count != 0):
        fiblast = fib - fiblast
    if (fib % 2 == 0):
        sumFib += fib
    count += 1

print(sumFib)
