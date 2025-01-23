class Person:
    def __init__(self, name: str, geschlecht: str):
        self.name = name
        self.geschlecht = geschlecht

class Mitarbeiter(Person):
    def __init__(self, name: str, geschlecht: str, abteilung: str):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name: str, geschlecht: str, abteilung: str):
        super().__init__(name, geschlecht, abteilung)

class Abteilung:
    def __init__(self, name: str):
        self.name = name
        self.mitarbeiter_liste = []
        self.leiter = None

    def setze_leiter(self, leiter: Abteilungsleiter):
        self.leiter = leiter
        self.mitarbeiter_liste.append(leiter)

    def füge_mitarbeiter_hinzu(self, mitarbeiter: Mitarbeiter):
        self.mitarbeiter_liste.append(mitarbeiter)

class Unternehmen:
    def __init__(self, name: str):
        self.name = name
        self.abteilungen = {}

    def füge_abteilung_hinzu(self, abteilung: Abteilung):
        self.abteilungen[abteilung.name] = abteilung

    def gesamt_mitarbeiter(self):
        return sum(len(abteilung.mitarbeiter_liste) for abteilung in self.abteilungen.values())

    def gesamt_leiter(self):
        return sum(1 for abteilung in self.abteilungen.values() if abteilung.leiter)

    def gesamt_abteilungen(self):
        return len(self.abteilungen)

    def größte_abteilung(self):
        return max(self.abteilungen.values(), key=lambda abt: len(abt.mitarbeiter_liste), default=None)

    def geschlechter_verhältnis(self):
        geschlechter = {}
        for abteilung in self.abteilungen.values():
            for mitarbeiter in abteilung.mitarbeiter_liste:
                geschlecht = mitarbeiter.geschlecht
                if geschlecht in geschlechter:
                    geschlechter[geschlecht] += 1
                else:
                    geschlechter[geschlecht] = 1
        
        gesamt = sum(geschlechter.values())
        return {geschlecht: anzahl / gesamt * 100 for geschlecht, anzahl in geschlechter.items()}

def main():
    unternehmen = Unternehmen("Piegger'scher Großbetrieb")

    abt1 = Abteilung("Schlachtung")
    abt2 = Abteilung("Verkauf")

    unternehmen.füge_abteilung_hinzu(abt1)
    unternehmen.füge_abteilung_hinzu(abt2)

    leiter1 = Abteilungsleiter("Hundegger", "Männlich", "Schlachtung")
    abt1.setze_leiter(leiter1)

    mitarbeiter1 = Mitarbeiter("Kelm", "Männlich", "Schlachtung")
    mitarbeiter2 = Mitarbeiter("Gräfin Wex", "Weiblich", "Schlachtung")
    abt1.füge_mitarbeiter_hinzu(mitarbeiter1)
    abt1.füge_mitarbeiter_hinzu(mitarbeiter2)

    leiter2 = Abteilungsleiter("Erika", "Weiblich", "Verkauf")
    abt2.setze_leiter(leiter2)

    mitarbeiter3 = Mitarbeiter("Warbeler", "Männlich", "Verkauf")
    abt2.füge_mitarbeiter_hinzu(mitarbeiter3)

    print(f"Gesamtmitarbeiter: {unternehmen.gesamt_mitarbeiter()}")
    print(f"Gesamtleiter: {unternehmen.gesamt_leiter()}")
    print(f"Gesamtabteilungen: {unternehmen.gesamt_abteilungen()}")
    größte_abt = unternehmen.größte_abteilung()
    print(f"Größte Abteilung: {größte_abt.name} mit {len(größte_abt.mitarbeiter_liste)} Mitarbeitern")
    print(f"Geschlechterverhältnis: {unternehmen.geschlechter_verhältnis()}")

if __name__ == "__main__":
    main()
