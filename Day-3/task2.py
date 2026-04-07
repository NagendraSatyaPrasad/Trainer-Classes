class Emp:
    total_salary = 0
    count = 0

    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

        Emp.total_salary += salary
        Emp.count += 1

    def __del__(self):
        Emp.total_salary -= self.salary
        Emp.count -= 1

    @classmethod
    def get_avg_salary(cls):
        if cls.count == 0:
            print("No employees")
        else:
            avg = cls.total_salary / cls.count
            print(avg)

e1 = Emp(name="ravi", dept="sales", salary=45000)
e2 = Emp("hari", "sales", 55000)
e3 = Emp("manu", "accts", 65000)

Emp.get_avg_salary()

e4 = Emp("emp1", "dept", 75000)
e5 = Emp("emp2", "dept", 85000)

Emp.get_avg_salary()

del e4
del e5

Emp.get_avg_salary()