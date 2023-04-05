"""
Jogo Palavra secreta - Tema comida
"""
palavra_secreta = "CHOCOLATE"
palpite = str(input("Informe seu palpite")).upper()
acertou = bool(palpite == palavra_secreta)
print("Acertou?",acertou)