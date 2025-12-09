import string
import random

# In-memory database
db = {}

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def save_url(long_url: str):
    code = generate_code()

    # ensure unique code
    while code in db:
        code = generate_code()

    db[code] = long_url
    return code

def get_url(code: str):
    return db.get(code)
