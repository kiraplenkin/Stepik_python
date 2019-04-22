import exceptions_2_2

print(exceptions_2_2.greet('Kirr'))

#  Task 4

import datetime

data = datetime.datetime.strptime(input(), "%Y %m %d")

new_day = datetime.timedelta(days=int(input()))
delta = data + new_day

print(delta.strftime("%Y %-m %-d"))
