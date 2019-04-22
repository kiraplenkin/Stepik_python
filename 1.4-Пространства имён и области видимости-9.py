def create(namespace, var):
    scopes.update({namespace: {'parent': var,
                               'variables': set()}})


def add(namespace, var):
    scopes[namespace]['variables'].add(var)


def get(namespace, var):
    try:
        if var in scopes[namespace]['variables']:
            return print(namespace)
        else:
            get(scopes[namespace]['parent'], var)
    except:
        return print(None)


scopes = {'global': {'parent': None,
                     'variables': set()}}

n = int(input())
for i in range(n):
    operation, namespace, var = input().split()
    if operation == 'create':
        create(namespace, var)
    elif operation == 'add':
        add(namespace, var)
    elif operation == 'get':
        get(namespace, var)
