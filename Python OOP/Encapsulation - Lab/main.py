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

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_valid_length = len(value) >= 8
        containing_upper_letter = [x for x in value if x.isupper()]
        containing_digit = [x for x in value if x.isdigit()]

        if not self.is_valid(is_valid_length, containing_upper_letter, containing_digit):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
