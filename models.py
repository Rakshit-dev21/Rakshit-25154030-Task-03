from abc import ABC , abstractmethod
class Employee(ABC):
    total_employee = 0
    def __init__(self , emp_id:str , name:str , department:str):
        if(emp_id.strip() == ""):
            raise ValueError("id cannot be empty")
        self.__emp_id = emp_id.strip()
        self.department = department
        if(name.strip() == ""):
            raise ValueError("Name cannot be empty")
        self.__name = name.strip()

    @property
    def emp_id(self):
        return self.__emp_id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self , name:str):
        if(name.strip() == ""):
            raise ValueError("Name cannot be empty")
        self.__name = name.strip()

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTime(Employee):
    def __init__(self, emp_id:str, name:str, department:str , monthly_salary:float , bonus:float = 0):
        super().__init__(emp_id, name, department)
        if(monthly_salary <= 0):
            raise ValueError("Salary cannot be 0 or negative") 
        self.__monthly_salary = monthly_salary
        if(bonus < 0):
            raise ValueError("Bonus cannot be negative")
        self.__bonus = bonus
        Employee.total_employee += 1
    @property
    def monthly_salary(self):
        return self.__monthly_salary       
    @monthly_salary.setter
    def monthly_salary(self , monthly_salary):
        if(monthly_salary <= 0):
            raise ValueError("Monthly Salary cannot be 0 or negative")
        self.__monthly_salary = monthly_salary

    @property
    def bonus(self):
        return self.__bonus       
    @bonus.setter
    def bonus(self , bonus):
        if(bonus < 0):
            raise ValueError("bonus cannot be negative")
        self.__bonus = bonus

    def calculate_salary(self):
        return self.__monthly_salary + self.__bonus

class PartTime(Employee):
    def __init__(self, emp_id:str, name:str, department:str , hourly_rate:float , hours_worked:float):
        super().__init__(emp_id, name, department) 
        if(hourly_rate <= 0):
            raise ValueError("Hourly Rate should be greater than 0")
        self.__hourly_rate = hourly_rate
        if(hours_worked < 0):
            raise ValueError("Hours cannot be negative")
        self.__hours_worked = hours_worked
        Employee.total_employee += 1
    @property
    def hourly_rate(self):
        return self.__hourly_rate        
    @hourly_rate.setter
    def hourly_rate(self , hourly_rate):
        if(hourly_rate <= 0):
            raise ValueError("Rate cannot be 0 or negative")
        self.__hourly_rate = hourly_rate

    @property
    def hours_worked(self):
        return self.__hours_worked
    @hours_worked.setter
    def hours_worked(self , hours_worked):
        if(hours_worked < 0):
            raise ValueError("Working Hours cannot be negative")
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked

class Intern(Employee):
    def __init__(self, emp_id:str, name:str, department:str , stipend:float):
        super().__init__(emp_id, name, department) 
        if(stipend <= 0):
            raise ValueError("stipend cannot be 0 or negative")
        self.__stipend = stipend
        Employee.total_employee += 1

    @property
    def stipend(self):
        return self.__stipend
    @stipend.setter
    def stipend(self , stipend):
        if(stipend <= 0):
            raise ValueError("stipend cannot be 0 or negative")
        self.__stipend = stipend


    def calculate_salary(self):
        return self.__stipend
    


        