class Employee:
    """Класс представления работников"""
    def __init__(self, first, last):
        self.first = first # нельзя использовать публично
        self.last = last # нельзя использовать публично

    @property
    def email(self):
        """Получение электронной почты пользователем"""
        return f'{self.first}_{self.last}.@gmail.com'

    @property
    def fullname(self):
        """Получение Имени и Фамилии пользователем"""
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, new_full_name):
        first, last = new_full_name.split(' ')
        self.first = first
        self.last =last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


if __name__ == '__main__':
    emp_1 = Employee('Arthur', 'Pyrkov')
    print(emp_1.first)
    print(emp_1.last)
    print(emp_1.email)
    print(emp_1.fullname)
    emp_1.fullname = 'Aleksey Ivanov'
    print(emp_1.fullname)
    del emp_1.fullname
    print(emp_1.fullname)