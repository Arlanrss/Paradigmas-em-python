try:
  letras = str(input("informe uma letra :")).upper()
  if letras == "A" or letras == "E" or letras == "I" or letras == "O" or letras == "U":
    print(f" A Letra {letras} é uma vogal")
  else:
    print(f"A letra {letras} e consoante")
except:
  Print("infome apenas letras")