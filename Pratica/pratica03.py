"""
Jogo Palavra secreta - Tema comida
"""
while True:
  palavra_secreta = "CHOCOLATE"
  palpite = str(input("Informe seu palpite")).upper()
  acertou = bool(palpite == palavra_secreta)

  if acertou:
    print("Parabéns você acertou")
    break
  else:
    print("Voce errou")