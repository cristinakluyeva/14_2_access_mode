class User:
    def __init__(self, name, password, is_admin = False):
        """конструктор, принимающий имя пользователя и пароль-name: свойство, которое возвращает имя пользователя"""

        self.name = name
        self.password = password
        self._is_logged_in = True
        self._is_admin = is_admin

    @property
    def _password(self):
        """позволяет установить или изменить пароль пользователя"""
        return self.password

    @_password.setter
    def _password(self, new_password):
        self.password = new_password

    @property
    def is_admin(self):
        """возвращает, является ли пользователь администратором или нет"""
        return self._is_admin

    def _is_admin(self, admin_status):
        """свойство-помощник, которое определяет, является ли пользователь администратором или нет"""
        if admin_status == self.is_admin:
            return True
        return False

    def login(self, user_password):
        """соответствует ли введенный пароль паролю пользователя"""
        if self.password == user_password:
            return True
        return False

    def logout(self):
        """выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)"""
        if self._is_logged_in:
            self._is_logged_in = False


# код для проверки
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1._password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1._password)  # newpassword

user1._is_admin = True
print(user1._is_admin)  # True

user1.login("newpassword")  # True
user1.logout()
