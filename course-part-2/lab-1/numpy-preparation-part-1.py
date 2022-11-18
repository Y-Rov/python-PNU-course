import numpy as np #1
f = [1, 7, 2, 4, 3] #2
x = np.array(f) #3
print(type(f), type(x)) #4

m = np.array([range(i, i + 5) for i in range(3)]) #5
print(m)

a = list(range(10)) #6
b = np.arange(10)
print(a, b)

a = a*5 #7
b = b*5
print(a, b)

a = list(map((lambda elem: pow(elem, 2)), a)) #8
b = b**2
print(a, b)

def addition(n):
    return n + 5

a = list(map(addition, a)) #9
b = b + 5
print(a, b)

list_mod = [elem % 2 for elem in a] #10
b = b % 2
print(list_mod, b)

c = np.array([2,2,6,4,5]) #11

#b == c #12
#b < c
#b > c

d = x + c #13
e = a + [1, 2, 3]
print(d, e, sep='\n')

print(c > 10) #14
print(c[c > 10])

print(c.sum()) #15
print(c.min())
print(c.max())

print(c.ndim) #16
print(c.shape)
print(c.size)
print(c.dtype)

b = np.arange(16).reshape(4, 4) #17
print(b)
print(b.sum(axis = 0))    #  Сума елементів кожного стовбця
print(b.sum(axis = 1))    #  Сума елементів кожного рядка
print(b.min(axis = 1))    #  Мінімальний елемент кожного рядка
print(b.max(axis = 0))    #  Максимальний елемент кожного стовбця

n = np.arange(0, 30, 2) #18
print(n)
n = n.reshape(3, 5)
print(n)
o = np.linspace(0, 4, 9)
print(o)
o.resize(3, 3)
print(o)
