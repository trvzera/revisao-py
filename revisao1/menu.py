import lerJson as ler

dados = ler.ler_arquivo()

racas = list(dados.keys())
def menu():
  for i, raca in enumerate(racas, start=1):
    print(f"{i} - {raca}") 

  op = int(input("Escolha a raça: "))

  raca_escolhida = racas[op-1]

  print(f"Você escolheu: {raca_escolhida}")
  print(f"Peso: {dados[raca_escolhida]}")
  return raca_escolhida