# Task 7


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.moneys = 0

    def can_add(self, v):
        if self.moneys + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.moneys += v


# Task 8

class Buffer:
    def __init__(self):
        self.count = 0
        self.sum = 0
        self.buf = []

    def add(self, *a):
        for i in range(len(a)):
            if self.count < 5:
                self.buf.append(a[i])
                self.count += 1
            else:
                self.sum = 0
                for n in range(len(self.buf)):
                    self.sum += self.buf[n]
                print(self.sum)
                self.buf = []
                self.count = 0
                self.sum = 0

    def get_current_part(self):
        return print(self.buf)  # ! Change to return self.buf


x = Buffer()
x.add(1, 2, 3, 4, 5, 6, 7)
x.get_current_part()

