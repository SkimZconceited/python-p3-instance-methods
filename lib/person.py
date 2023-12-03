#!/usr/bin/env python3

class Person:
    # Class body goes here
    def __init__(self) -> None:
        pass

    #Instance method definition
    def talk(self):
        print('Hello World!')
        pass

    def walk(self):
        print('The person is walking.')
        pass
    pass

guido = Person()
print(type(guido.talk))
