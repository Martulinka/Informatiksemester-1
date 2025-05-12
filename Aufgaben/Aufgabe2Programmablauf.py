import random
Würfel = [1, 2 , 3, 4, 5, 6]
AnzahlWürfe = 0
while AnzahlWürfe < 3 or Wurf == 6:

  Wurf = random.choice(Würfel)
  print(Wurf)
  AnzahlWürfe = AnzahlWürfe + 1
  
  if Wurf == 6: 
      print("Sechs geworfen!")
      AnzahlWürfe = 3 
      continue
