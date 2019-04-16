# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
# пространства <namespace>, или None, если такого пространства не существует

# add global a
# create foo global
# add foo b


def create(namespace, var):
    scopes.update({namespace: {'parent': var, 'variables': set()}})


def add(namespace, var):
    scopes[namespace]['variables'].add(var)


def get(namespace, var):
    pass


n = int(input())

scopes = {'global': {'parent': None, 'variables': set()}}

for i in range(n):
    operation, namespace, var = input().split()
    if operation == 'create':
        create(namespace, var)
    elif operation == 'add':
        add(namespace, var)
    elif operation == 'get':
        get(namespace, var)

    print(scopes.items())

