try:
  primeiro = int(input('Primeiro numero: '))
  segundo  = int(input('Segundo numero : '))
  terceiro = int(input('Terceiro numero: '))
  
  maior = primeiro
  
  if (segundo > maior):
   maior = segundo
  if (terceiro > maior):
     maior = terceiro
  
  print(f"Maior:  {maior}")
except ValueError:
  print("Informe apenas numeros")