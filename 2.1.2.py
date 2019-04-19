class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, item):
        if item > 0:
            super(PositiveList, self).append(item)
        else:
            raise NonPositiveError
