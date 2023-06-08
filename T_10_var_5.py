class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class StateMachine:
    state = 'A'

    def crash(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'G':
            self.state = 'A'
            return 9
        elif self.state == 'B':
            self.state = 'G'
            return 2
        elif self.state == 'C':
            self.state = 'F'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise(MealyError('crash'))

    def place(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise(MealyError('place'))


def main():
    return StateMachine()


def test():
    sm = main()

    sm.state = 'A'
    try:
        sm.place()
    except MealyError:
        pass

    sm.state = 'E'
    try:
        sm.crash()
    except MealyError:
        pass

    sm.state = 'F'
    try:
        sm.crash()
    except MealyError:
        pass

    sm.state = 'G'
    try:
        sm.place()
    except MealyError:
        pass

    sm.state = 'A'
    assert sm.crash() == 0
    assert sm.state == 'B'

    sm.state = 'B'
    assert sm.place() == 1
    assert sm.state == 'C'

    sm.state = 'B'
    assert sm.crash() == 2
    assert sm.state == 'G'

    sm.state = 'C'
    assert sm.place() == 3
    assert sm.state == 'D'

    sm.state = 'C'
    assert sm.crash() == 4
    assert sm.state == 'F'

    sm.state = 'D'
    assert sm.place() == 6
    assert sm.state == 'F'

    sm.state = 'D'
    assert sm.crash() == 5
    assert sm.state == 'E'

    sm.state = 'E'
    assert sm.place() == 7
    assert sm.state == 'F'

    sm.state = 'F'
    assert sm.place() == 8
    assert sm.state == 'G'


o = main()
print(o.crash())
print(o.place())
print(o.crash())
print(o.place())
print(o.crash())
print(o.crash())
print(o.crash())
print(o.crash())
print(o.crash())
print(o.place())
print(o.place())
print(o.crash())
print(o.place())
print(o.place())





