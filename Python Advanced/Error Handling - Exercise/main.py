from homework.custom_exeptions import NameTooShortError, MustContainAtSymbolError, InvalidDomainError


def is_valid_length(current_mail):
    username = current_mail.split("@")[0]

    if len(username) < 4:
        return False

    return True


def contain_symbols(current_mail):
    count = current_mail.count("@")
