async def encrypt_password(password):
    encrypted_password = ""

    for character in password:
        new_character = chr(ord(character) + 3)
        encrypted_password += new_character


    return encrypted_password

async def decrypt_password(password): 
    decrypted_password = ""

    for character in password:
        new_character = chr(ord(character) - 3)
        decrypted_password += new_character


    return decrypted_password
