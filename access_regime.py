class Employee:
    """Класс представления работников"""
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.__first = first # нельзя использовать публично
        self.__last = last # нельзя использовать публично
        self._email= f'{first}_{last}.@gmail.com' #Защищаем переменную. Использовать ее можно, но менять публично нельзя
        self.pay = pay

    def full_name(self):
        return f'{self.__first} {self.__last}'


if __name__ == '__main__':
    emp_1 = Employee('Richard', 'Rich', 1300000)
    #print(emp_1.__first)
    #print(emp_1.__last)
    print(emp_1.full_name())
    print(emp_1._email)
    print(emp_1.pay)