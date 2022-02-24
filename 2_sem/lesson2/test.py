class A:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        '''=='''
        return self.value == other.value

    def __ne__(self, other):
        """!="""
        pass

    def __lt__(self, other):
        """<"""
        return True

    def __le__(self, other):
        """<="""

    """gt (>), ge(>=)"""


a1 = A(6)
a2 = A(5)

print(a1 == a2)
