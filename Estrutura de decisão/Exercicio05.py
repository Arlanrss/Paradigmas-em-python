nota1 = float(input("Informe a primera nota: "))
nota2 = float(input("Informe a segunda nota: "))


if (nota1 > 0 and nota1 <= 10) and (nota2 > 0 and nota2 <= 10):
  media = (nota1 + nota2) / 2
  print(f"A média foi {media:.1f}")
  
  
  if media >= 6 and media < 10:
    print("Você foi aprovado!")
  elif media == 10:
    print("Aprovado com destinção")
  else:
    print("Reprovado")