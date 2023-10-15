numero = int(input("Digite um número inteiro: "))

if numero <= 0:
    print("O número deve ser maior que zero.")
else:
    print(f"Números ímpares de 1 até {numero}:")
    for i in range(1, numero + 1, 2):
        print(i)
