# Kasus 1 Encapsulation

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_password(self):
        return "*****"

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            print("Password Updated Succesfully") 
        else:
            print("Password must be al least 8 characters")

user = User("Fadlan Hussein", "Secure 123")
print(user.username)
print(user.get_password())
user.set_password("NewPassword")