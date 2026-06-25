import asyncio

async def validate_email(email):
    if await email.count('@') != 1 or email.count('.com') != 1:
        return False
    return True

