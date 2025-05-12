Optionen = ["Geld" , "Pasch"]
Würfeln = [1, 2, 3, 4, 5, 6]
import random
random.choice(Optionen)
if random.choice(Optionen) == "Geld":
    print("Ich nehme das Geld")
    print("Du bist frei")
else:
    AnzahlWürfe = 0
    while AnzahlWürfe < 3:
        AnzahlWürfe = AnzahlWürfe + 1
        Wurf = random.choice(Würfeln)
        print(Wurf)
        Wurf2 = random.choice(Würfeln)
        print(Wurf2)
        Wurf3 = random.choice(Würfeln)
        print(Wurf3)
        if Wurf == Wurf2 == Wurf3:
            print("Pasch")
            continue
        if AnzahlWürfe == 3 and Wurf != Wurf2 != Wurf3:
            print("Du musst zahlen")
            

    
    

