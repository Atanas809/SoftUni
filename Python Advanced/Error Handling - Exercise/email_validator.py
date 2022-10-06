#  You need to import exeptions from 'custom_exeptions' file!!!
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


email = input()
valid_domains = [".com", ".bg", ".org", ".net"]

while email != "End":

    if not is_valid_length(email):
        raise NameTooShortError("Name must be more than 4 characters")
    elif not contain_symbols(email):
        raise MustContainAtSymbolError("Email must contain one '@'.")
    elif not valid_domain(email, valid_domains):
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")
    else:
        print("Email is valid")

    email = input()
