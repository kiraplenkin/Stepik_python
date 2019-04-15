############################
print('\nTask 9')

# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
# пространства <namespace>, или None, если такого пространства не существует

# add global a
# create foo global
# add foo b


def create(namespace, parent):
    pass


def add(namespace, var):
    pass


def get(namespace, var):
    pass


n = int(input())

parent_namespaces = {
    'None': 'global'
}

child_namespaces = {
    'global': []
}

for i in range(n):
    operation, namespace, arg = input().split()
    if operation == 'create':
        create(namespace, parent)
    elif operation == 'add':
        add(namespace, var)
    elif operation == 'get':
        get(namespace, var)

    print(child_namespaces.items())

