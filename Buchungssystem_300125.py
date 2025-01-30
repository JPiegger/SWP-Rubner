class Room:
    total_rooms = 0  

    def __init__(self, zimmertyp, pProNacht):
        Room.total_rooms += 1 
        self.nummer = Room.total_rooms 
        self.zimmertyp = zimmertyp
        self.pProNacht = pProNacht
        self.gebucht = False

    def book_room(self):
        if self.gebucht:
            return f"Zimmer {self.nummer} ist belegt!"
        else:
            self.gebucht = True
            return f"Buchung Zimmer {self.nummer} erfolgreich!"

    def cancel_booking(self):
        if not self.gebucht:
            return f"Zimmer {self.nummer} war nicht gebucht!"
        else:
            self.gebucht = False
            return f"Zimmer {self.nummer} storniert!"
        
    def __str__(self):
        return f"Zimmernummer: {self.nummer}, Gebucht? {self.gebucht}, Preis: {self.pProNacht}€, Typ: {self.zimmertyp}"
        
class Hotel:
    def __init__(self, name):
        self.name = name
        self.zimmer = []

    def buchen(self, nummer):
        for z in self.zimmer:
            if z.nummer == nummer:
                print(z.book_room())
                return 
        print(f"Zimmer {nummer} existiert nicht!")

    def stornieren(self, nummer):
        for z in self.zimmer:
            if z.nummer == nummer:
                print(z.cancel_booking())
                return 
        print(f"Zimmer {nummer} existiert nicht!")
    
    def anzahl_freie_zimmer(self):
        freie_zimmer = sum(1 for z in self.zimmer if not z.gebucht)
        return f"Anzahl der freien Zimmer: {freie_zimmer}"
    

def main():
    z1 = Room("Einzel", 339.98)
    z2 = Room("Doppel", 529.98)

    print(z1)

    grandhotel = Hotel("Plaza-City")
    grandhotel.zimmer.append(z1)
    grandhotel.zimmer.append(z2)

    print(grandhotel.anzahl_freie_zimmer())
    
    grandhotel.buchen(1)
    grandhotel.buchen(3)

    print(grandhotel.anzahl_freie_zimmer())
    
    grandhotel.stornieren(1)
    grandhotel.stornieren(2)
    grandhotel.stornieren(3)

    print(grandhotel.anzahl_freie_zimmer())

if __name__ == "__main__":
    main()
