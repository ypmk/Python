class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class StateMachine:
    state = 'A'

    def paste(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'F':
            self.state = 'F'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise(MealyError('paste'))

    def link(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'H'
            return 9
        else:
            raise(MealyError('link'))

    def run(self):
        if self.state == 'A':
            self.state = 'G'
            return 11
        elif self.state == 'D':
            self.state = 'F'
            return 5
        elif self.state == 'F':
            self.state = 'G'
            return 7
        else:
            raise (MealyError('run'))

    def loop(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        else:
            raise(MealyError('loop'))


def main():
    return StateMachine()


def test():
    sm = main()

    sm.state = 'A'
    try:
        sm.run()
    except MealyError:
        pass

    sm.state = 'A'
    try:
        sm.loop()
    except MealyError:
        pass

    sm.state = 'B'
    try:
        sm.paste()
    except MealyError:
        pass

    sm.state = 'B'
    try:
        sm.link()
    except MealyError:
        pass

    sm.state = 'B'
    try:
        sm.run()
    except MealyError:
        pass

    sm.state = 'C'
    try:
        sm.run()
    except MealyError:
        pass

    sm.state = 'C'
    try:
        sm.loop()
    except MealyError:
        pass

    sm.state = 'C'
    try:
        sm.paste()
    except MealyError:
        pass

    '''
    продолжение
    '''

    sm.state = 'A'
    assert sm.paste() == 0
    assert sm.state == 'B'

    sm.state = 'B'
    assert sm.loop() == 2
    assert sm.state == 'C'

    '''
    продолжение
    '''

o=main()
print(o.loop())
