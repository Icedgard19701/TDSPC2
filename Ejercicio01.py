n = []
m = []
p = []

for i in range(0,3):
    b = int(input("Inserte numeros para la primera fila: "))
    n.append(b)
    
for i in range(0,3):
    b = int(input("Inserte numeros para la segunda fila: "))
    m.append(b)
    
for i in range(0,3):
    b = int(input("Inserte numeros para la tercera fila: "))
    p.append(b)
    
suma = n[0] + m[1] + p[2]

if suma % 2 == 0:
    print("La suma de elementos en su diagonal principal es par")
else:
    print("La suma de elementos en su diagonal principal es impar")

 