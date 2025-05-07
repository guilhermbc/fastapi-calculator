#Retorna a adição de dois floats
def add(a: float, b: float) -> float:
    return a + b

#Retorna a subtração de dois floats
def subtract(a: float, b: float) -> float:
    return a - b

#Retorna a multiplicação de dois floats
def multiply(a: float, b: float) -> float:
    return a * b

#Retorna a divisão de dois floats
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

#Retorna a raiz quadrada de um float
# Se o número for negativo, levanta um ValueError
def sqrroot(a: float) -> float:
    if a < 0:
        raise ValueError("Raiz quadrada de número negativo não é permitida.")
    return a ** 0.5

#Retorna a potência de um float elevado a outro float
def power(a: float, b: float) -> float:
    return a ** b