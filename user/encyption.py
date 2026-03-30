def encyption_password (password):
    encyption_password = ""
    for character in password:
          new_character = chr(ord(character)+3)
          encyption_password += new_character
    return encyption_password

def decrypt_password (password):
    decrypt_password = ""
    
    for character in password:
        new_character = chr(ord(character)-3)
        decrypt_password += new_character
    return decrypt_password


