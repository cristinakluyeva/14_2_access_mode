import datetime


class Employee:
    """Класс представления работников"""
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email= f'{first}_{last}.@gmail.com'
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @classmethod
    def set_raise_amt(cls, new_raise_amt):
        cls.raise_amt = new_raise_amt

    @staticmethod
    def is_workday(data):
        if data.weekday() == 5 or data.weekday() == 6:
            return False
        return True



if __name__ == '__main__':
    emp_1 = Employee('Марина', 'Егорова', 113000)
    emp_1_str = 'Карина-Клюева-240000'
    emp_2 = Employee.from_string(emp_1_str)
    print(emp_1.first, emp_1.last, emp_1.pay, emp_1.email)
    print(emp_2.first, emp_2.last, emp_2.pay, emp_2.email)
    Employee.set_raise_amt(1.15)
    print(Employee.raise_amt)
    my_date = datetime.date(2025, 3, 9)
    print(Employee.is_workday(my_date))