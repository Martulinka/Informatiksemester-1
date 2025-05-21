energie_kwh = float(input("Geben Sie den Energieverbrauch in kWh an: "))
Heizdauer = float(input("Geben Sie die Heizdauer in h an: "))
tarif = input("Geben Sie den Tarif an (Erdgas, Strom, Heizöl): ")
def berechne_kosten(energie_kwh, tarif, Heizdauer):
    erdgas_preis = 0.09* energie_kwh* Heizdauer
    strom_preis = 0.30 * energie_kwh * Heizdauer
    heizöl_preis = 0.11 * energie_kwh * Heizdauer
    return erdgas_preis, strom_preis, heizöl_preis  
print("Die Heizkosten betragen:")
berechne_kosten(energie_kwh, tarif, Heizdauer)