import secrets
import string

length = int(input("password length: "))
use_symbols = input("include symbols? (y/n): ").lower().startswith("y")

chars = string.ascii_letters + string.digits
if use_symbols:
    chars += string.punctuation

password = "".join(secrets.choice(chars) for _ in range(length))
print(password)
