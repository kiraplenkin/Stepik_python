def list_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result


def sum(a, b):
    return a + b


y = sum(14, 29)
z = list_sum([1, 2, 3])

print(y)
print(z)


###########################
print('\nTask 5')


def g():
    print('I am in function g')


def f():
    print('I am in function f')
    g()
    print('I am in function f')


print('I am outside of any function')
f()
print('I am outside of any function')


############################
print('\nTask 6')


x = [1, 2, 3]

x.append(4)
x.append(5)

print(x)
top = x.pop()
print(top)
print(x)

top = x.pop()
print(top)
print(x)
