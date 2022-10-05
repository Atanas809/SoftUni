from homework.custom_exeptions import NameTooShortError, MustContainAtSymbolError, InvalidDomainError


def is_valid_length(current_mail):
    username = current_mail.split("@")[0]

    if len(username) < 4:
        return False

    return True


def contain_symbols(current_mail):
    count = current_mail.count("@")

    if count == 1:
        return True

    return False


def valid_domain(current_mail, valid_domains):
    data = current_mail.split("@")[1]

    domain = f'.{data.split(".")[-1]}'

    if domain in valid_domains:
        return True

    return False
