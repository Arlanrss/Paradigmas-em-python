
print("Bem vindo a escola")
turno = str(input("informe o turno \n M = manhã \n V= vesperino \n N = noite \n")).upper()
if turno == "M" or turno == "V" or turno == "N":
  if turno == "M":
    print("Bom dia!\n Bom estudo")
  if turno == "V":
    print("Boa tarde!\n Bom estudo.")
  if turno == "N":
    print("Boa noite!\n Bom estudo")
else:
  print("Erro\n Informe apenas, M para manhã, V para vesperino e N para noite")
