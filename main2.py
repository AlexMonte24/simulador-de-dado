import random, time

resultados = []
print("Bem-vindo ao")
print("Simulador de Dado!")
print("-------------------")

time.sleep(1)

print("Você precisa fazer no mínimo 20 pontos para ganhar, Terá 5 chances. Boa sorte!")

def rolar_dado():
    for i in range(5):
        dado = random.randint(1, 6)
        print(f"Valor do Dado: {dado}")
        time.sleep(0.5)
        resultados.append(dado)
        
def calcular_pontos():
    return sum(resultados)

while True:
    time.sleep(1)
    print("Rolando os dados...")
    time.sleep(0.5)
    rolar_dado()
    resultado = calcular_pontos()
    print(f"O resultado é: {resultado}")
    time.sleep(1)
    if resultado >= 20:
        print("Parabéns! Você ganhou!")
    else:
        print("Que pena! Você perdeu!")
        
    resposta = input("Deseja jogar novamente? (s/n): ").lower()
    if resposta == 's':
        resultados.clear()
        continue
    else:
        print(f"Seus resultados foram: {resultados}")
        time.sleep(1)
        print("Até a próxima!")
        print("Obrigado por jogar!")
        print("-------------------")
        exit()
