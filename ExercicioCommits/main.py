import os

def celsiusParaFahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheitParaCelcios(fahrenheit):
    return (fahrenheit -32) * 5/9

def main():
    while True:
        print("Bem-vindo ao conversor de temperatura")
        escolha = input("Digite 'C' para converter Celsios para Fhrenheit ou 'F' para converter Fahrenheit para Celsius (ou 'Q' para sair): ").upper()

        if escolha == 'C':
            temperaturaCelsius = float(input("Digite o valor em celsius: "))
            temperaturaFahrenheit = celsiusParaFahrenheit(temperaturaCelsius)
            print(f"{temperaturaCelsius}ºC é igual a {temperaturaFahrenheit}ºF")
        elif escolha == 'F':
            temperaturaFahrenheit = float(input("Digite o valor em fahrenheit: "))
            temperaturaCelsius = fahrenheitParaCelcios(temperaturaFahrenheit)
            print(f"{temperaturaFahrenheit}ºF é igual a {temperaturaCelsius}ºC")
        elif escolha == 'Q':
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida, por favor execute o programa novamente e escolha 'C', 'F' ou 'Q'.")

        input("Pressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()