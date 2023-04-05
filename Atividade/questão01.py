try:
  print("Eleiçoes 2024")
  idade = int(input("informe sua idade para votação:"))
  if idade >= 16:
    print("idade valida para votação")
  else:
    print("Idade invalida para vota")
except ValueError:
  print("Idade invalida, informe apenas numeros, tente novamente!")