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
        self.buf = []

    def add(self, *a):
        i = 0
        while i < len(a):
            self.buf.append(a[i])
            if len(self.buf) >= 5:
                self.sum = 0
                for n in range(len(self.buf)):
                    self.sum += self.buf[n]
                print(self.sum)
                self.buf = self.buf[5:]
            i += 1

    def get_current_part(self):
        return self.buf
