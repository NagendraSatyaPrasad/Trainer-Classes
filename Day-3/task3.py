class Emp:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    def __eq__(self, other):
        return (self.name == other.name and
                self.dept == other.dept and
                self.salary == other.salary)

    def __str__(self):
        return f'Emp("{self.name}","{self.dept}",{self.salary})'

    def __lt__(self, other):
        return self.salary < other.salary


e1 = Emp("ravi", "sales", 25000)
e2 = Emp("ravi", "sales", 25000)

if e1 == e2:
    print("they are same")
else:
    print("they are distinct")

print(e1)
print(e2)

emps = []
emps.append(e1)
emps.append(Emp("manu1", "accts", 55000))
emps.append(Emp("manu2", "sales", 45000))
emps.append(Emp("manu3", "purch", 65000))
emps.append(Emp("manu4", "finan", 35000))

emps.sort()

for e in emps:
    print(e)