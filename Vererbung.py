class Landmaschine:
    def __init__(self, hersteller, modell, baujahr):
        if not hersteller or not modell:
            raise ValueError("Hersteller und Modell sind erforderlich.")  # Typ (c): Fehler nicht behebbar
        self.hersteller = hersteller
        self.modell = modell
        self.baujahr = baujahr or "Unbekannt"  # Typ (a): Neuer Fehler behebbar

    def beschreibung(self):
        return f"{self.hersteller} {self.modell} (Baujahr: {self.baujahr})"

    def starten(self):
        print(f"{self.beschreibung()} wird gestartet.")

    def stoppen(self):
        print(f"{self.beschreibung()} wird gestoppt.")


class Traktor(Landmaschine):
    def __init__(self, hersteller, modell, baujahr, ps):
        super().__init__(hersteller, modell, baujahr)
        if not isinstance(ps, (int, float)) or ps <= 0:
            raise ValueError("PS muss eine positive Zahl sein.")  # Typ (c): Fehler nicht behebbar
        self.ps = ps

    def beschreibung(self):
        return super().beschreibung() + f", {self.ps} PS"

    def pfluegen(self):
        try:
            print(f"{self.beschreibung()} pflügt das Feld.")
        except Exception as e:
            print(f"Fehler beim Pflügen: {e}")  # Typ (b): Hochblubber-Fehler behebbar


class Mähdrescher(Landmaschine):
    def __init__(self, hersteller, modell, baujahr, schneidwerksbreite):
        super().__init__(hersteller, modell, baujahr)
        self.schneidwerksbreite = schneidwerksbreite or 0.0  # Typ (a): Neuer Fehler behebbar

    def beschreibung(self):
        return super().beschreibung() + f", Schneidwerksbreite: {self.schneidwerksbreite} m"

    def ernten(self):
        try:
            print(f"{self.beschreibung()} erntet das Getreide.")
        except Exception as e:
            print(f"Fehler beim Ernten: {e}")  # Typ (b): Hochblubber-Fehler behebbar


class Forwarder(Landmaschine):
    def __init__(self, hersteller, modell, baujahr, ladekapazitaet):
        super().__init__(hersteller, modell, baujahr)
        if ladekapazitaet <= 0:
            raise ValueError("Ladekapazität muss größer als 0 sein.")  # Typ (c): Fehler nicht behebbar
        self.ladekapazitaet = ladekapazitaet

    def beschreibung(self):
        return super().beschreibung() + f", Ladekapazität: {self.ladekapazitaet} Tonnen"

    def holz_transportieren(self):
        print(f"{self.beschreibung()} transportiert Holz.")


# CLI-Fehlerbehandlung - Typ (d): Hochblubber-Fehler nicht behebbar
import sys

def main():
    traktor = Traktor("Fendt", "Vario 724", 2020, 240)
    traktor.starten()
    traktor.pfluegen()
    traktor.stoppen()

    maehdrescher = Mähdrescher("Claas", "Lexion 780", 2019, 13)
    maehdrescher.starten()
    maehdrescher.ernten()
    maehdrescher.stoppen()

    forwarder = Forwarder("John Deere", "1210G", 2021, 21)
    forwarder.starten()
    forwarder.holz_transportieren()
    forwarder.stoppen()

def my_cli():
    try:
        main()
    except Exception as error:
        print(f"Unerwarteter Fehler: {error}")
        sys.exit(1)

if __name__ == "__main__":
    my_cli()
