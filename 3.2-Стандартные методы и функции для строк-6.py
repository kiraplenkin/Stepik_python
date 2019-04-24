s = str(input())
a = str(input())
b = str(input())

i = 0
while True:
    while i <= 1000 and a in s:
        s = s.replace(a, b)
        i += 1
    else:
        if i > 1000:
            print('Impossible')
            break
        else:
            print(i)
            break
