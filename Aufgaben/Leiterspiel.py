Spielbrett = {0: "Start", 3: "Leiter nach oben 10", 5: "Schlange nach unten 3", 8: "Leiter nach oben 22", 10: "Schlange nach unten 5", 20: "Leiter nach oben 15", 24: "Schlange nach unten 10", 40: "Leiter nach oben 20", 45: "Schlange nach unten 15", 98: "Schlange nach unten 20", 100: "Ziel"}
Würfeln = (1, 2, 3, 4, 5, 6)
import random
Position = 0
while Position < 100:
            Würfelwurf = random.choice(Würfeln)
            print(Würfelwurf)
if Position + random.choice(Würfeln) == Spielbrett[3]:
		print("Du bist auf dem Feld 3, die Leiter befördert dich um 10 Felder nach oben")
		Position = Position + 10
		if Position + random.choice(Würfeln) == Spielbrett[5]:
                         print("Du bist auf dem Feld 5, die Schlange befördert dich um 3 Felder nach unten")
Position = Position - 3
if Position + random.choice(Würfeln) == Spielbrett[8]:
            print("Du bist auf dem Feld 8, die Leiter befördert dich um 22 Felder nach oben")
            Position = Position + 22
if Position + random.choice(Würfeln) == Spielbrett[10]:
            print("Du bist auf dem Feld 10, die Schlange befördert dich um 5 Felder nach unten")
            Position = Position - 5
            if Position + random.choice(Würfeln) == Spielbrett[20]:
                    print("Du bist auf dem Feld 20, die Leiter befördert dich um 15 Felder nach oben")
            Position = Position + 15    
            if Position + random.choice(Würfeln) == Spielbrett[24]:
                    print("Du bist auf dem Feld 24, die Schlange befördert dich um 10 Felder nach unten")       
            Position = Position - 10
            if Position + random.choice(Würfeln) == Spielbrett[40]:
                    print("Du bist auf dem Feld 40, die Leiter befördert dich um 20 Felder nach oben")      
            Position = Position + 20        
            if Position + random.choice(Würfeln) == Spielbrett[45]:
                    print("Du bist auf dem Feld 45, die Schlange befördert dich um 15 Felder nach unten")       
            Position = Position - 15    
            if Position + random.choice(Würfeln) == Spielbrett[98]:
                    print("Du bist auf dem Feld 98, die Schlange befördert dich um 20 Felder nach unten")   
            Position = Position - 20    
            if Position + random.choice(Würfeln) == Spielbrett[100]:
                    print("Du bist auf dem Feld 100, du hast das Ziel erreicht")
                    continue
if Position + random.choice(Würfeln) > 100:
        print("Du bist auf dem Feld 100, du hast das Ziel erreicht")
        
