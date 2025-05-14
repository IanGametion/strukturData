# Nama File: condition.py

from stack3 import Queue

class Condition(object):
    def __init__(self, rank):
        self.rank = rank
        
    def __ge__(self, other): # Membandingkan prioritas
        return self.rank >= other.rank
    
    def __str__(self):
        if self.rank == 1:
            return "critical"
        elif self.rank == 2:
            return "serious"
        else:
            return "fair"