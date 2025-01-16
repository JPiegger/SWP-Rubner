class Auto:
    def __init__(self, ps):
        if not isinstance(ps, (int, float)) or ps < 0:
            raise ValueError("PS muss eine nicht-negative Zahl sein.")
        self.ps = ps

    def __add__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Addition ist nur zwischen Auto-Objekten erlaubt.")
        return Auto(self.ps + other.ps)

    def __sub__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Subtraktion ist nur zwischen Auto-Objekten erlaubt.")
        return Auto(self.ps - other.ps)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Multiplikation ist nur mit Zahlen erlaubt.")
        return Auto(self.ps * other)

    def __eq__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps == other.ps

    def __lt__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps < other.ps

    def __gt__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps > other.ps

    def __len__(self):
        return int(self.ps)

    def __repr__(self):
        return f"Auto({self.ps} PS)"

def main():
    a1 = Auto(50)
    a2 = Auto(60)
    print(a1 + a2)
    print(a2 - a1)
    print(a1 * 2)
    print(a1 == a2)
    print(a1 < a2)
    print(a1 > a2)
    print(len(a1))
    try:
        print(a1 + 10)
    except TypeError as e:
        print(e)
    try:
        print(a1 - "test")
    except TypeError as e:
        print(e)
    try:
        print(a1 * a2)
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()