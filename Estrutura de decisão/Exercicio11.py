try:
  salario = float(input("Informe seu salario :"))
  
  aumento = 100
  
  if salario <= 280:
   aumento = 20
  elif salario <= 700:
    aumento = 15
  elif salario <= 1.500:
    aumento = 10
  else:
    aumento = 5

  reajuste = (salario * aumento)/100
  novosalario = salario + reajuste
  
  print(f"salario antigo {salario:.2f} \n Aumento percetual de {aumento} \n Valor do aumento {reajuste:.2f} \n salario novo e {novosalario:.2f}  ")
except ValueError:
  print("Erro \n Informe apenas numeros")