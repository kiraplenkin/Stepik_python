import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, item):
        super(LoggableList, self).append(item)
        self.log(item)
