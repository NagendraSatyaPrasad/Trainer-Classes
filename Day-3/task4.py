class Number:
    def __init__(self, num):
        self.num = num

    def show(self):
        print(f"Number: {self.num}")

    def convert(self):
        print("No conversion available")


class Binary(Number):
    def show(self):
        print(f"Binary: {bin(self.num)}")

    def convert(self):
        print(f"{self.num} -> Binary = {bin(self.num)}")


class Octal(Number):
    def show(self):
        print(f"Octal: {oct(self.num)}")

    def convert(self):
        print(f"{self.num} -> Octal = {oct(self.num)}")


class Hexa(Number):
    def show(self):
        print(f"Hexa: {hex(self.num)}")

    def convert(self):
        print(f"{self.num} -> Hexa = {hex(self.num)}")

res = [
    Binary(25),
    Octal(30),
    Hexa(256),
    Octal(15),
    Number(25)
]

for e in res:
    e.show()
    e.convert()
    