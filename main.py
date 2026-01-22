def mostrar_menu():
    print("\n=== SISTEMA DE LÓGICA EM PYTHON ===")
    print("1 - Calculadora")
    print("2 - Conversor de Temperatura")
    print("3 - Verificar número par ou ímpar")
    print("0 - Sair")


def calculadora():
    print("\n--- Calculadora ---")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Escolha a operação: ")

    if opcao == "1":
        print("Resultado:", a + b)
    elif opcao == "2":
        print("Resultado:", a - b)
    elif opcao == "3":
        print("Resultado:", a * b)
    elif opcao == "4":
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Erro: divisão por zero")
    else:
        print("Opção inválida")


def conversor_temperatura():
    print("\n--- Conversor de Temperatura ---")
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")


def par_ou_impar():
    print("\n--- Verificar Par ou Ímpar ---")
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print("O número é PAR")
    else:
        print("O número é ÍMPAR")


def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            calculadora()
        elif escolha == "2":
            conversor_temperatura()
        elif escolha == "3":
            par_ou_impar()
        elif escolha == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


main()
