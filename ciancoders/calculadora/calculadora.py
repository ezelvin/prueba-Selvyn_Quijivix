def resolver_operacion(expresion):
    if len(expresion) > 20:
        return "No puede ser superior a 20 caracteres"

    numeros = []
    operadores = []
    numero_actual = ""
    for caracter in expresion:
        if caracter.isdigit() or caracter == ".":
            numero_actual += caracter
        else:
            numeros.append(float(numero_actual))
            numero_actual = ""
            operadores.append(caracter)
    numeros.append(float(numero_actual))

    ii = 0
    while ii < len(operadores):
        if operadores[ii] == "*":
            resultado = numeros[ii] * numeros[ii + 1]
            del numeros[ii]
            numeros[ii] = resultado
            del operadores[ii]
        elif operadores[ii] == "/":
            if numeros[ii + 1] == 0:
                return "Error: División por cero no permitida."
            resultado = numeros[ii] / numeros[ii + 1]
            del numeros[ii]
            numeros[i] = resultado
            del operadores[ii]
        else:
            ii += 1

    resultado = numeros[0]
    for i in range(1, len(numeros)):
        if operadores[i-1] == "+":
            resultado += numeros[i]
        elif operadores[i-1] == "-":
            resultado -= numeros[i]

    return resultado


# Ejemplo de uso
expresion = input("Ingrese una cadena de numeros: ")
resultado = resolver_operacion(expresion)
print("Resultado:", resultado)
