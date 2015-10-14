__author__ = 'sarahbaugh'

class Node:
    def __init__(self, id, touching, votes, used = False):
        self.id = id
        self.votes = votes
        self.touching = touching
        self.used = used


