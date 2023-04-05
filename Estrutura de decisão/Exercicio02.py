try:
  numero = float(input("Informe um nunmero \n"))
  if numero > 0:
    print(" É positivo")
  else:
      print("É negativo")
except ValueError:
  print("Erro, Informe apenas numeros inteiros.")