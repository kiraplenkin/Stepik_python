exceptions = {}


def add_exception(exceptions, exception_name, exception_parents):
    if exception_name not in exceptions:
        exceptions[exception_name] = []
    exceptions[exception_name].extend(exception_parents)
    for parent in exception_parents:
        if parent not in exceptions:
            exceptions[exception_parents] = []


n = int(input())

for _ in range(n):
    exception_description = input().split()
    exception_name = exception_description[0]
    exception_parents = exception_description[2:]
    add_exception(exceptions, exception_name, exception_parents)


print(exceptions)  # TODO finish him
