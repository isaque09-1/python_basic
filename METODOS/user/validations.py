def validate_email(email):
    if email.count('@') != 1 or email.count('.com') != 1:
        return False
    return True

print(validate_email('emailsergio@'))
print(validate_email('cristina.com'))
print(validate_email('email@email.com'))