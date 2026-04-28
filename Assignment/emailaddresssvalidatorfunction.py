def email_validation(email_address):

    if len(email_address) < 8:
        return False

    if "@" not in email_address:
        return False

    if email_address.startswith("@") or email_address.endswith("@"):
        return False

    return True
