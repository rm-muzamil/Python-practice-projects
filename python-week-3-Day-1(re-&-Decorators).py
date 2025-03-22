import re

pattren = r"\+\d++-\d++-\d+"

text = "My Numbers is +0309-187-7204 and +0328-055-1204"


match = re.findall(pattren,text)
print(match)

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.search(pattern, email))

print(is_valid_email("test@example.com"))  # ✅ True
print(is_valid_email("invalid-email"))     # ❌ False

def is_valid_username(username):
    pattren = r"^[a-zA-Z]+[a-zA-Z0-9]+$"
    return bool(re.search(pattren,username))
print(is_valid_username("rm099"))
print(is_valid_username("8srm099"))






