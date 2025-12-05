# calculadora.py
# Autor: Gina Fernanda Bosiga

def calcular(numero_1, numero_2, operacion):
    """Realiza una operación matemática entre dos números."""
    if operacion == '+':
        return numero_1 + numero_2
    elif operacion == '-':
        return numero_1 - numero_2
    elif operacion == '*':
        return numero_1 * numero_2
    elif operacion == '/':
        if numero_2 != 0:
            return numero_1 / numero_2
        else:
            return "Error: no se puede dividir por cero."
    elif operacion == '%':  # NUEVA OPERACIÓN (módulo)
        return numero_1 % numero_2
    else:
        return "Operación no válida."

def main():
    try:
        numero_1 = float(input("Primer número: "))
        numero_2 = float(input("Segundo número: "))
        operacion = input("Operación (+, -, *, /, %): ").strip()

        resultado = calcular(numero_1, numero_2, operacion)
        print("Resultado:", resultado)

    except ValueError:
        print("Error: por favor ingrese solo números válidos.")

if __name__ == "__main__":
    main()