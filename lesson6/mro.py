"""
def __eq__()
MRO
"""


class A:

    def __init__(self, a):
        self.a = a

    def some_func(self):
        print('A')

    def __eq__(self, other):
        return self.a == other.a

    def __str__(self):
        return 'Class A'

a1 = A(5)
a2 = A(6)

print(str(a1))
print(a1 == a2)



# class B(A):
#     def some_func(self):
#         print('B')
#
#
# class C(B, A):
#     pass

#

# class O:
#     pass
# class A(O):
#     pass
# class B(O):
#     pass
# class C(O):
#     pass
# class D(O):
#     pass
# class E(O):
#     pass
# class K1(A, B, C):
#     pass
# class K2(B, D):
#     pass
# class K3(C, D, E):
#     pass
# class Z(K1, K2, K3):
#     pass


# print(Z.mro())
