print("Ordem descrecente dos numeros")
try:
  v1 = float(input('Primeiro numero: '))
  v2 = float(input('Segundo numero : '))
  v3 = float(input('Terceiro numero: '))
  
  if v1 <= v2 and v1 <= v3 and v2 <= v3:
    print (f" A ordem decresente dos valores são {v1}, {v2} , {v3}")
  if v1 <= v2 and v1 <= v3 and v3 <= v2:
   print (f" A ordem decresente dos valores são {v1}, {v3} , {v2}") 
  if v2 <= v1 and v2 <= v3 and v1 <= v3:
   print (f" A ordem decresente dos valores são {v2}, {v1} , {v3}") 
  if v2 <= v1 and v2 <= v3 and v3 <= v1:
   print (f" A ordem decresente dos valores são {v2}, {v3} , {v1}")
  if v3 <= v1 and v3 <= v2 and v1 <= v2:
   print (f" A ordem decresente dos valores são {v3}, {v1} , {v2}")
  if v3 <= v1 and v3 <= v2 and v2 <= v1:
   print (f" A ordem decresente dos valores são {v3}, {v2} , {v1}")
except ValueError:
  print("Erro \n Informe apenas numeros ")