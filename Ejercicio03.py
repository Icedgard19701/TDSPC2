import random

m = []
n = [1,2,3,4,5,6,7,8,9,10]
p = []

y = 0


for i in range(0,6):
    a = int(input("Ingrese su numero a jugar: "))
    q = p.count(a)
    if q == 1:
        print("Ya ingreso ese numero:")
    else:
        m.append(a)

for j in range(0,6):
    z = random.choice(n)
    n.remove(z)
    p.append(z)

for k in range(0,6):
    z = 0
    s = p.count(m[z])
    z = z + 1
    if s == 1:
        print("Va 1")

print(p)
print(m[1])
