# Ejercicio 1
D = {"a": "Teclado", "b": "Mouse", "c": "Pantalla"}
D.setdefault("d","CPU")
print(D)

# Ejercicio 2
D = {"c": "mochila", "u": "Lapiz"}
D.setdefault("j","lapicero")
print(D)

# Ejercicio 3
D = {"c": "Pantalla"}
D.setdefault("e","camara")
print(D)

# Ejercicio 4
D = {"g": "USB", "m": "Ram", "n":"ROM"}
D.setdefault("p","motherboard")
print(D)

# Ejercicio 5
D = {}
D.setdefault("i","pycharm")
print(D)

# Ejercicio 6
D = {"e": "Bateria", 1: "celular"}
D.setdefault("k","cargador")
print(D)

# Ejercicio 7
D = {"nota": 12, "nota2": 13, "nota3": 14, "nota4":15}
D.setdefault("nota5", 16)
print(D)

# Ejercicio 8
D = {1: "Hola", 2: "hello"}
D.setdefault(3, "Hi")
print(D)

# Ejercicio 9
D = {"Z": 27, "a": 1}
D.setdefault("m", 14)
print(D)

# Ejercicio 10
D = {10: "ayuda"}
D.setdefault(20, "help")
print(D)