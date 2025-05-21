def EingabeDerWerte():
  print("Geben Sie die Raumbreite an")
  Raumbreite=float(input ("Raumbreite"))
  print("Geben Sie die Raumhöhe an")  
  Raumhöhe=float(input ("Raumhöhe"))
  print("Geben Sie die Raumhöhe an")  
  Raumlänge=float(input ("Raumlänge"))
  print("Geben Sie die Außentemperatur an")   
  Raumtemperatur=float(input ("Raumtemperatur"))
  print("Geben Sie die Außentemperatur an")   
  Außentemperatur=float(input ("Außentemperatur"))
  V= Raumbreite*Raumhöhe*Raumlänge    
  dT= Raumtemperatur-Außentemperatur
  return V, dT    

V, dT =EingabeDerWerte()
def Funktion(V, dT):
  P= V*dT*0.024
  print("Die Heizleistung beträgt", P, "kW")  
  return P

P= Funktion()

import temperatur
from temperatur import celsius_to_kelvin, celsius_to_fahrenheit

celsius=float(input("Geben Sie die Temperatur in Celsius an: "))    
kelvin = celsius_to_kelvin(celsius)
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C sind {kelvin}K und {fahrenheit}°F")

