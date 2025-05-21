Spielbrett = {0: "Start", 3: "Leiter nach oben 10", 5: "Schlange nach unten 3", 8: "Leiter nach oben 22", 10: "Schlange nach unten 5", 20: "Leiter nach oben 15", 24: "Schlange nach unten 10", 40: "Leiter nach oben 20", 45: "Schlange nach unten 15", 98: "Schlange nach unten 20", 100: "Ziel"}
Würfeln = (1, 2, 3, 4, 5, 6)
import random
Position = 0
anzahl_würfe = 0
while Position < 100:
            anzahl_würfe+=1
            Würfelwurf = random.choice(Würfeln)
            print(Würfelwurf)
            Position=Position+Würfelwurf+Spielbrett[Position+Würfelwurf]      
if Position + random.choice(Würfeln) > 100:
        print("Du bist auf dem Feld 100, du hast das Ziel erreicht")    
        
