# Ejercicio 1
D = {"a": "Teclado", "b": "Mouse", "c": "Pantalla"}
X = D.pop("c")
print(D)
print(X)

# Ejercicio 2
D = {"c": "mochila", "u": "Lapiz"}
X = D.pop("j", "error")
print(D)
print(X)

# Ejercicio 3
D = {"c": "Pantalla", "d": "camara", "e": "radar"}
X = D.popitem()
print(D)
print(X)

# Ejercicio 4
D = {"g": "USB", "m": "Ram", "n":"ROM"}
X = D.popitem()
print(D)
print(X)

# Ejercicio 5
D = {1: "azul", 2:"verde", 3:"rojo"}
X = D.pop(4, "error")
print(D)
print(X)

# Ejercicio 6
D = {"e": "Bateria", 1: "celular"}
X = D.pop(1)
print(D)
print(X)


# Ejercicio 7
D = {"nota": 12, "nota2": 13, "nota3": 14, "nota4":15}
X = D.pop("nota9", "error")
print(D)
print(X)

# Ejercicio 8
D = {1: "Hola", 2: "hello"}
X = D.popitem()
print(D)
print(X)

# Ejercicio 9
D = {"Z": 27, "a": 1}
X = D.pop("Z")
print(D)
print(X)

# Ejercicio 10
D = {10: "ayuda", 11:"Salvenme", 12:"peligro"}
X = D.pop(12)
print(D)
print(X)