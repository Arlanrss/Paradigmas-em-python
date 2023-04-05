"""
Jogo Palavra secreta - Tema comida
"""
print("-------Jogo Palavra secreta - Tema comida-------")
print("voce tere 3 tentativas")
palavra_secreta = "CHOCOLATE"

for tentativas in range(1, 4):
  print(f"{tentativas}°Tentativas")
  palpite = str(input("Informe seu palpite: ")).upper()
  acertou = bool(palpite == palavra_secreta)
  if acertou:
    print("Parabéns você acertou")
    break
  else:
    print("Voce errou")