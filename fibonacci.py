def fibonacci(numero):
    
    if numero < 0:
        return False
    n1 = 0
    n2 = 1
    
    if numero == n1 or numero == n2:
        return True
    
    while n2 < numero:
        n1, n2 = n2, n1 + n2
    
    return n2 == numero

while True:
    num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    if fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
        print("---> FIM")
        break
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")
        print("-"*30)
        print("Digite outro número!")

