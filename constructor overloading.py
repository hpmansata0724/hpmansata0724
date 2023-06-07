class employee:
    company="google"
    def __init__(self,name="rajesh",salary=3000):
        self.name=name
        self.salary=salary
    def getdetails(self):
        print("The name of employee is",self.name)
        print("The salary of employee is",self.salary)
e1=employee("Raj",10000)
e2.employee("Mahesh")
e3=employee()
print("Employee's details of",employee.company,"company")
e1.getdetails()
e5.getdetails()
e3.getdetails()