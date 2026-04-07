class Emp:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    def show(self):
        print(f"name={self.name} dept={self.dept} salary={self.salary}")

    def compare_dept(self, other):
        return self.dept == other.dept

e1 = Emp(name="ravi", dept="sales", salary=45000)
e2 = Emp("hari", "sales", 56000)

e1.show()
e2.show()

if e1.compare_dept(e2):
    print("They work for same dept")
else:
    print("They work in diff depts")