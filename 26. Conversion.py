# Ejercicio 1
D = {"a": "Teclado", "b": "Mouse", "c": "Pantalla"}
l = list(D) + list(D.values())
print(l, type(l))

# Ejercicio 2
D = {"c": "mochila", "u": "Lapiz"}
t = tuple(D) + tuple(D.values())
print(t, type(t))

# Ejercicio 3
D = {"c": "Pantalla"}
s = set(D).union(set(D.values()))
print(s, type(s))

# Ejercicio 4
D = {"g": "USB", "m": "Ram", "n":"ROM"}
t = tuple(D) + tuple(D.values())
print(t, type(t))

# Ejercicio 5
D = {1: 10, 2: 20, 3:30}
t = tuple(D) + tuple(D.values())
print(t, type(t))

# Ejercicio 6
D = {"e": "Bateria", 1: "celular"}
s = set(D).union(set(D.values()))
print(s, type(s))

# Ejercicio 7
D = {"nota": 12, "nota2": 13, "nota3": 14, "nota4":15}
s = set(D).union(set(D.values()))
print(s, type(s))

# Ejercicio 8
D = {1: "Hola", 2: "hello"}
l = list(D) + list(D.values())
print(l, type(l))

# Ejercicio 9
D = {"Z": 27, "a": 1}
s = set(D).union(set(D.values()))
print(s, type(s))

# Ejercicio 10
D = {10: "ayuda"}
l = list(D) + list(D.values())
print(l, type(l))