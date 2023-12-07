class employee:
    empid = 0
    empname = ''
    empadress = ''
    empsalary = 0

    def getdata(self):
        return str(self.empid) +";"+ self.empname + ";" + self.empadress + ";" + str(self.empsalary)

    def printdata(self):
        print(self.getdata())

emp1 = employee()
emp1.empid = 111
emp1.empname = 'ahmed'
emp1.empadress = 'algiers'
emp1.empsalary = 2000
emp1.printdata()


emp2 = employee()
emp2.empid = 222
emp2.empname = 'adel'
emp2.empadress = 'giza'
emp2.empsalary = 2500
emp2.printdata()

emp3 = employee()
emp3.empid = 333
emp3.empname = 'amr'
emp3.empadress = 'egypt'
emp3.empsalary = 2200
emp3.printdata()

        
     
      
