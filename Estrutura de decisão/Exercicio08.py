try:
  print("Consulta de preços")
  valor1 = float(input('Informe o primeiro valo: '))
  valor2  = float(input('Informe o segundo  valor: '))
  valor3 = float(input('Informe o terceiro valor: '))
  
  if valor1 < valor2 and valor1 < valor3:
    print("Voce deve compra o primeiro produto")
  elif valor2 < valor1 and valor2 < valor3:
    print("Você deve compra o segundo produto")
  elif valor3 < valor1 and valor3 < valor2:
    print("Você deve comprar o terceito produto")
  else:
    print("Informe um valor valido")
except ValueError:
  print(" ERRO\n Informe apenas preços validos")