class Landmaschine:
    def __init__(self, hersteller, modell, baujahr):
        self.hersteller = hersteller
        self.modell = modell
        self.baujahr = baujahr

    def beschreibung(self):
        return f"{self.hersteller} {self.modell} (Baujahr: {self.baujahr})"

    def starten(self):
        print(f"{self.beschreibung()} wird gestartet.")

    def stoppen(self):
        print(f"{self.beschreibung()} wird gestoppt.")


class Traktor(Landmaschine):
    def __init__(self, hersteller, modell, baujahr, ps):
        super().__init__(hersteller, modell, baujahr)
        self.ps = ps

    def beschreibung(self):
        return super().beschreibung() + f", {self.ps} PS"

    def pfluegen(self):
        print(f"{self.beschreibung()} pflügt das Feld.")


class Mähdrescher(Landmaschine):
    def __init__(self, hersteller, modell, baujahr, schneidwerksbreite):
        super().__init__(hersteller, modell, baujahr)
        self.schneidwerksbreite = schneidwerksbreite

    def beschreibung(self):
        return super().beschreibung() + f", Schneidwerksbreite: {self.schneidwerksbreite} m"

    def ernten(self):
        print(f"{self.beschreibung()} erntet das Getreide.")


class Forwarder(Landmaschine):
    def __init__(self, hersteller, modell, baujahr, ladekapazitaet):
        super().__init__(hersteller, modell, baujahr)
        self.ladekapazitaet = ladekapazitaet

    def beschreibung(self):
        return super().beschreibung() + f", Ladekapazität: {self.ladekapazitaet} Tonnen"

    def holz_transportieren(self):
        print(f"{self.beschreibung()} transportiert Holz.")
        

# Beispielverwendung
if __name__ == "__main__":
    traktor = Traktor("Fendt", "Vario 724", 2020, 240)
    maehdrescher = Mähdrescher("Claas", "Lexion 780", 2019, 550)
    forwarder = Forwarder("John Deere", "1210G", 2021, 210)

    traktor.starten()
    traktor.pfluegen()
    traktor.stoppen()

    maehdrescher.starten()
    maehdrescher.ernten()
    maehdrescher.stoppen()

    forwarder.starten()
    forwarder.holz_transportieren()
    forwarder.stoppen()
