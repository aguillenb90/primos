def primos_hasta_100():
    primos = []
    for num in range(2, 101):  # empezamos en 2 porque 0 y 1 no son primos
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos

# Ejemplo de uso
print(primos_hasta_100())
