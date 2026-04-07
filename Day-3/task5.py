class Emp:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.isalpha():
            self._name = value
        else:
            self._name = "NoName"

    def show(self):
        print(f"name={self.name} city={self.city}")

e1 = Emp("ravi", "blr")
e1.show()

e1.name = "arun1"
e1.show()

e1.name = "arun"
e1.show()

e2 = Emp("hari123", "chn")
e2.show()