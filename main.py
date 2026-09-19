from models import *
employees = []
emp1 = FullTime(2020 , 'Rakshit' , 'CS' , 50000, 10000)
emp2 = PartTime(2018 , 'Pranjal' , 'ECE' , 1000 , 10 )
emp3 = Intern(2017 , 'Arjun' , 'CSE' , 40000)
employees.append(emp1)
employees.append(emp2)
employees.append(emp3)
for i in range(0 , len(employees)):
    print(list[i].name , list[i].calculate_salary())

print(Employee.total_employee)
