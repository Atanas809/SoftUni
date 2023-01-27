class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def is_valid(self, is_valid_length, containing_upper_letter, containing_digit):
        if is_valid_length and containing_upper_letter and containing_digit:
            return True
        return False

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value
