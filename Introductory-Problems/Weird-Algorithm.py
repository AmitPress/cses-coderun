n = int(input())

while True:  
    if n == 1:
        print(1)
        break
    else:
        print(int(n), end=' ')
    if n%2 == 0:
        n /= 2
    else:
        n = n * 3 + 1


