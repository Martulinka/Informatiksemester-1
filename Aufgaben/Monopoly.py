Optionen = ["Geld" , "Pasch"]
Würfeln = [1, 2, 3, 4, 5, 6]
import random
random.choice(Optionen)
if random.choice(Optionen) == "Geld":
    print("Ich nehme das Geld")
    print("Du bist frei")
else:
    print("Ich nehme nicht das Geld")
    AnzahlWürfe = 0
    while AnzahlWürfe < 3:
        AnzahlWürfe = AnzahlWürfe + 1
        Wurf1 = random.choice(Würfeln)
        print(Wurf1)
        Wurf2 = random.choice(Würfeln)
        print(Wurf2)
        Wurf3 = random.choice(Würfeln)
        print(Wurf3)
        if Wurf1 == Wurf2 == Wurf3:
            print("Pasch")
            print("Du bist frei")
            AnzahlWürfe = 3
            continue
        if AnzahlWürfe == 3 and Wurf1 != Wurf2 != Wurf3:
            print("Du musst zahlen")
            

    
    

