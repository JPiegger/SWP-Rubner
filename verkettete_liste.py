class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.next_elem = None

    def set_next_elem(self, next_elem):
        self.next_elem = next_elem

    def get_next_elem(self):
        return self.next_elem

    def get_obj(self):
        return self.obj


class EinfachVerketteteListe:
    def __init__(self):
        self.start_elem = ListElement("Kopf")

    def add_last(self, obj):
        new_elem = ListElement(obj)
        last_elem = self.get_last_elem()
        last_elem.set_next_elem(new_elem)

    def insert_after(self, prev_item, new_item):
        pointer_elem = self.start_elem.get_next_elem()
        while pointer_elem is not None and pointer_elem.get_obj() != prev_item:
            pointer_elem = pointer_elem.get_next_elem()
        if pointer_elem is not None:
            new_elem = ListElement(new_item)
            next_elem = pointer_elem.get_next_elem()
            pointer_elem.set_next_elem(new_elem)
            new_elem.set_next_elem(next_elem)

    def delete(self, obj):
        le = self.start_elem
        while le.get_next_elem() is not None:
            if le.get_next_elem().get_obj() == obj:
                if le.get_next_elem().get_next_elem() is not None:
                    le.set_next_elem(le.get_next_elem().get_next_elem())
                else:
                    le.set_next_elem(None)
                break
            le = le.get_next_elem()

    def find(self, obj):
        le = self.start_elem
        while le is not None:
            if le.get_obj() == obj:
                return True
            le = le.get_next_elem()
        return False

    def get_first_elem(self):
        return self.start_elem

    def get_last_elem(self):
        le = self.start_elem
        while le.get_next_elem() is not None:
            le = le.get_next_elem()
        return le

    def write_list(self):
        le = self.start_elem
        while le is not None:
            print(le.get_obj())
            le = le.get_next_elem()


if __name__ == "__main__":
    liste = EinfachVerketteteListe()
    liste.add_last("1")
    liste.add_last("2")
    liste.add_last("3")
    liste.add_last("4")
    liste.add_last("5")
    liste.insert_after("2", "neu")
    liste.delete("3")
    liste.write_list()
    print("Erstes Element:", liste.get_first_elem().get_obj())
    print("Ist '3' enthalten?", liste.find("3"))
    print("Ist '5' enthalten?", liste.find("5"))
    print("Letztes Element:", liste.get_last_elem().get_obj())