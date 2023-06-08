class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class StateMachine:
    state = 'A'

    def reset(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'D':
            self.state = 'B'
            return 6
        elif self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise(MealyError('reset'))

    def tread(self):
        if self.state == 'B':
            return 3
        elif self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        else:
            raise(MealyError('tread'))

    def roam(self):
        if self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise(MealyError('roam'))


def main():
    return StateMachine()


def test():
    sm = main()

    sm.state = 'A'
    try:
        sm.roam()
    except MealyError:
        pass

    sm.state = 'B'
    try:
        sm.roam()
    except MealyError:
        pass
    sm.state = 'C'
    try:
        sm.roam()
    except MealyError:
        pass
    sm.state = 'C'
    try:
        sm.reset()
    except MealyError:
        pass
    sm.state = 'D'
    try:
        sm.roam()
    except MealyError:
        pass
    sm.state = 'E'
    try:
        sm.reset()
    except MealyError:
        pass
    sm.state = 'E'
    try:
        sm.tread()
    except MealyError:
        pass
    sm.state = 'F'
    try:
        sm.roam()
    except MealyError:
        pass
    sm.state = 'F'
    try:
        sm.tread()
    except MealyError:
        pass

    sm.state = 'A'
    assert sm.reset() == 0
    assert sm.state == 'B'
    sm.state = 'A'
    assert sm.tread() == 1
    assert sm.state == 'D'
    sm.state = 'B'
    assert sm.reset() == 2
    assert sm.state == 'C'
    sm.state = 'B'
    assert sm.tread() == 3
    assert sm.state == 'B'
    sm.state = 'C'
    assert sm.tread() == 4
    assert sm.state == 'D'
    sm.state = 'D'
    assert sm.reset() == 6
    assert sm.state == 'B'
    sm.state = 'D'
    assert sm.tread() == 5
    assert sm.state == 'E'
    sm.state = 'E'
    assert sm.roam() == 7
    assert sm.state == 'F'
    sm.state = 'F'
    assert sm.reset() == 8
    assert sm.state == 'D'


o = main()
print(o.tread())
print(o.reset())
print(o.tread())
print(o.roam())