class immigrationvisa:
    immvisatype="Express Entry Visa"
    fees=200000
    salary=10000
    def getimmvisatypedetails(self):
        print("This is",self.immvisatype)

class studentvisa:
    stuvisatype="student visa"
    fees=50000
    salary=20000
    def getstuvisatypedetails(self):
        print("This is",self.stuvisatype)


class employee(immigrationvisa,studentvisa):
    company="Newyork visa world"
    country="canada"
    salary=0
    def detdetails(self):
        print("He is an employee of",self.company)
        print("He works in",self.immvisatype,"and",self.stuvisatype,"category for",self.country,"country")
    def totalsalary(self):
        self.salary=immigrationvisa.salary+studentvisa.salary
        print("Total salary=.",self.salary)
e=employee()
e.getimmvisatypedetails()
e.getstuvisatypedetails()

print("fees::",e.fees)
e.totalsalary()

