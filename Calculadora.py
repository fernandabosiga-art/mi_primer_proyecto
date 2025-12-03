# calculadora.py
# Autor: Gina Fernanda Bosiga

n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
op = input("Operación (+, -, *, /): ")

if op == "+":
    print("Resultado:", n1 + n2)
elif op == "-":
    print("Resultado:", n1 - n2)
elif op == "*":
    print("Resultado:", n1 * n2)
elif op == "/":
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Error: no se puede dividir por cero.")
else:
    print("Operación no válida.")