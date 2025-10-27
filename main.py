import random, time

resultados = []

print("Bem-vindo ao")
print("Simulador de Dado!")
print("-------------------")

def rolar_dado():
    return random.randint(1, 6)
  
while True:
    time.sleep(1)
    print("Rolando o dado...")
    time.sleep(0.5)
    resultado = rolar_dado()
    resultados.append(resultado)
    print(f"O resultado é: {resultado}")
    time.sleep(1)
    resposta = input("Deseja jogar novamente? (s/n): ").lower()
    if resposta == 's':
        continue
    else:
        print(f"Seus resultados foram: {resultados}")
        time.sleep(1)
        print("Até a próxima!")
        print("Obrigado por jogar!")
        print("-------------------")
        exit()
        