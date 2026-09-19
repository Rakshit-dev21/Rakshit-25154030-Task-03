from abc import ABC , abstractmethod
class Employee(ABC):
    total_employee = 0
    def __init__(self , id , name , department):
        self.id = id
        self.name = name
        self.department = department
        Employee.total_employee += 1

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTime(Employee):
    def __init__(self, id, name, department , monthly_salary , bonus = 0):
        super().__init__(id, name, department) 
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus

class PartTime(Employee):
    def __init__(self, id, name, department , hourly_rate , hours_worked):
        super().__init__(id, name, department) 
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Intern(Employee):
    def __init__(self, id, name, department , stipend):
        super().__init__(id, name, department) 
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend
    


        