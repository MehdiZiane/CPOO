class A:
    def z(self):
        return self
    def y(self, t):
        return len(t)

a = A
Y = a.z
aa = a()
print(aa is a())
z = aa.y
print(z(()))
print(a().y((a, )))
print(A.y(aa, (a,z)))
print(aa.y((z, 1, 'z')))