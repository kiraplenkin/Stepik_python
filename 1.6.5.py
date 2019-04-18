n = int(input())

lst_mro = []
lst_q = []

for i in range(n):
    lst_mro.append(input().split(':'))

k = int(input())

for i in range(k):
    lst_q.append(input().split())


print(lst_mro[1][1])
print(lst_q)

for i in range(len(lst_q)):
    pass