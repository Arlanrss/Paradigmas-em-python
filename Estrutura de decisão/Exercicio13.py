try:
  dia = int(input("dugite um numero de 1 a 7 :"))
  
  if dia == 1:
    print (f"{dia} domingo")
  elif dia == 2:
    print (f"{dia} segunda")
  elif dia == 3:
    print (f"{dia} Terça")
  elif dia == 4:
    print (f"{dia} Quarta")
  elif dia == 5:
    print (f"{dia} quinta")
  elif dia == 6:
    print (f"{dia} Sexta")
  elif dia == 7:
    print (f"{dia} Sabado")
  else:
    print("Informe apenas numeros de 1 a 7")
except ValueError:
  print("Informe apenas numeros")