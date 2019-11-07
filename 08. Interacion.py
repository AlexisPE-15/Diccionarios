# Ejercicio 1
D = {"a": "Teclado", "b": "Mouse", "c": "Pantalla"}
for K in D:
    print(K)

# Ejercicio 2
D = {"c": "mochila", "u": "Lapiz"}
for K in D:
    print(D[K])

# Ejercicio 3
D = {"c:": "Pantalla", "d:": "camara", "e:": "radar"}
for k,v in zip(D.keys(), D.values()):
    print(k,v)

# Ejercicio 4
D = {"g": "USB", "m": "Ram", "n":"ROM"}
for k,v in D.items():
    print(k,v)

# Ejercicio 5
D = {1: "azul", 2:"verde", 3:"rojo"}
for k,v in D.items():
    print(k,v)

# Ejercicio 6
D = {"e": "Bateria", 1: "celular"}
for k,v in zip(D.keys(), D.values()):
    print(k, v)

# Ejercicio 7
D = {"nota": 12, "nota2": 13, "nota3": 14, "nota4":15}
for a, b in D.items():
    print(a, b)

# Ejercicio 8
D = {1: "Hola", 2: "hello"}
for i in D:
    print(D[i])

# Ejercicio 9
D = {"Z": 27, "a": 1}
for K in D:
    print(K)

# Ejercicio 10
D = {10: "ayuda", 11:"Salvenme", 12:"peligro"}
for k, v in D.items():
    print(k, v)