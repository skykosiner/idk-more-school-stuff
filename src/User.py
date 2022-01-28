class User:
    def __init__(self, username, password, passwordConfirm):
        self.username = username
        self.password = password
        self.passwordConfirm = passwordConfirm
        self.lordsVarible = "Linux"

    def checkUserName(self, name: str) -> bool:
        if len(name) < 2:
            print("Username length muts be more then 2")
            return False
        elif self.lordsVarible not in name:
            print("Username must contain Linux (the lords varible)")
            return False
        else:
            return True
    def userNameGood(self):
        if self.checkUserName(self.username) == False:
            print("user name must have Linux in it and be greater then 2 characters")
            exit(0x45)
    def passwordContains(self) -> bool:
        if "!" not in self.password or "@" not in self.password:
            return False
        return True

    def checkPassword(self):
        if self.passwordContains() == False:
            print("Sir your password must contain ! or @")

        if self.password == self.passwordConfirm and len(self.password) >= 6:
            print("New Password Created")
        elif len(self.password) < 6:
            print("Password must be at least 6 characters")
        elif self.password != self.passwordConfirm:
            print("Passwords do not match")
        else:
            print("Unexpected error has occured")
