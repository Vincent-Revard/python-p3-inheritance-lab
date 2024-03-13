#!/usr/bin/env python

from user import User

class Student(User):
    '''Student class'''

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, knowledge):
        '''Learn a piece of knowledge'''
        self.knowledge.append(knowledge)