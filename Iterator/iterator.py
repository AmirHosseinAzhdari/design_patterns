"""Iterator (Behavioral)
    1- Iterable, 2-Iteration
        __iter__, __next__

It is used for special sequences

"""


class Iteration:
    """ Print values from last to first"""

    def __init__(self, value):
        self._value = value

    def __next__(self):
        if self._value == 0:
            raise StopIteration("End of sequence ...")
        for i in range(0, self._value):
            value = self._value
            self._value -= 1
            return value


class Iterable:

    def __init__(self, value):
        self._value = value

    def __iter__(self):
        return Iteration(self._value)


f1 = Iterable(5)
f2 = iter(f1)

print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
