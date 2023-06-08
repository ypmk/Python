class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class StateMachine:
    state = 'A'

    def fetch(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        else:
            raise(MealyError('fetch'))

    def pull(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 4
        else:
            raise(MealyError('pull'))

    def crash(self):
        if self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'A':
            self.state = 'H'
            return 2
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise(MealyError('crash'))

    def coast(self):
        if self.state == 'A':
            self.state = 'F'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'G':
            self.state = 'D'
            return 10
        else:
            raise(MealyError('coast'))


def main():
    return StateMachine()


def test():
    sm = main()

    sm.state = 'B'
    try:
        sm.fetch()
    except MealyError:
        pass

    sm.state = 'B'
    try:
        sm.crash()
    except MealyError:
        pass

    sm.state = 'B'
    try:
        sm.coast()
    except MealyError:
        pass

    sm.state = 'C'
    try:
        sm.coast()
    except MealyError:
        pass

    sm.state = 'C'
    try:
        sm.fetch()
    except MealyError:
        pass

    sm.state = 'C'
    try:
        sm.pull()
    except MealyError:
        pass

    sm.state = 'D'
    try:
        sm.fetch()
    except MealyError:
        pass

    sm.state = 'D'
    try:
        sm.pull()
    except MealyError:
        pass

    sm.state = 'D'
    try:
        sm.crash()
    except MealyError:
        pass

    sm.state = 'E'
    try:
        sm.coast()
    except MealyError:
        pass

    sm.state = 'E'
    try:
        sm.fetch()
    except MealyError:
        pass

    sm.state = 'E'
    try:
        sm.pull()
    except MealyError:
        pass

    sm.state = 'F'
    try:
        sm.coast()
    except MealyError:
        pass

    sm.state = 'F'
    try:
        sm.fetch()
    except MealyError:
        pass

    sm.state = 'F'
    try:
        sm.pull()
    except MealyError:
        pass

    sm.state = 'G'
    try:
        sm.pull()
    except MealyError:
        pass

    sm.state = 'G'
    try:
        sm.fetch()
    except MealyError:
        pass

    sm.state = 'H'
    try:
        sm.coast()
    except MealyError:
        pass

    sm.state = 'H'
    try:
        sm.fetch()
    except MealyError:
        pass

    sm.state = 'H'
    try:
        sm.pull()
    except MealyError:
        pass

    sm.state = 'A'
    assert sm.fetch() == 1
    assert sm.state == 'A'

    sm.state = 'A'
    assert sm.pull() == 0
    assert sm.state == 'B'

    sm.state = 'A'
    assert sm.coast() == 3
    assert sm.state == 'F'

    sm.state = 'A'
    assert sm.crash() == 2
    assert sm.state == 'H'

    sm.state = 'B'
    assert sm.pull() == 4
    assert sm.state == 'C'

    sm.state = 'C'
    assert sm.crash() == 5
    assert sm.state == 'D'

    sm.state = 'D'
    assert sm.coast() == 6
    assert sm.state == 'E'

    sm.state = 'E'
    assert sm.crash() == 7
    assert sm.state == 'F'

    sm.state = 'F'
    assert sm.crash() == 8
    assert sm.state == 'G'

    sm.state = 'G'
    assert sm.crash() == 9
    assert sm.state == 'H'

    sm.state = 'C'
    assert sm.crash() == 5
    assert sm.state == 'D'

    sm.state = 'H'
    assert sm.crash() == 11
    assert sm.state == 'F'

o=main()
print(o.fetch())
print(o.pull())
print(o.pull())
print(o.crash())
print(o.coast())
print(o.crash())
print(o.pull())


