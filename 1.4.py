############################
print('\nTask 9')

# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
# пространства <namespace>, или None, если такого пространства не существует

# add global a
# create foo global
# add foo b

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
        pass child_namespaces[arg]
    elif operation == 'add':
        pass # child_namespaces[namespace] = arg
    elif operation == 'get':
        pass

    print(child_namespaces.items())

