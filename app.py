from src import User

username = str(input("Enter your username: "))
password = str(input("Password: "))
passwordConfirm = str(input("Password: "))

User = User(username, password, passwordConfirm)
User.userNameGood()
User.checkPassword()
