print("Alo Mundo")

  if numero > numero2 and numero3:
    print(f"O numero {numero} é o maior valor")
  elif numero2 > numero and numero3:
    print(f"O numero {numero2} é o maior valor")
  elif numero and numero2 < numero3:
   print(f"O numero {numero3} é o maior valor")   
  else:
    print("Erro, informe apenas numeros")
except ValueError: 
  print("Erro, informe apenas numeros inteiros")