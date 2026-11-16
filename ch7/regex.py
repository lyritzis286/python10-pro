"""Kanonikes ekfraseis (regular expressions)"""

import re

text = """Πρωτη συναντηση: 2021-01-01 και 2η συναντηση: 2022-12-31.
"""

#Όλα τα ματσις που ταιριαζουν με την ημερομηνία
pattern  = r"\d{2}-\d{2}-\d{4}"
matches = re.findall(pattern, text)
print(f"Βρεθηκαν οι ημερομηνιες: {matches}")

#Ολα τα matches με groups
pattern = r"(\d{2})-(\d{2})-(\d{4})"
matches = re.findall(pattern, text)
for day, mont, year in matches: #list of tuples
    print(f"Ημερα: {day}, Μηνας: {mont}, Χρονος: {year}")


#full match - validates the entire string
date = "01-01-2026"
if re.fullmatch(pattern, date):
    print(f"{date} is a valid date")


#fullmatch - validates the entire string
date = "01-01-2026"
match = re.fullmatch(pattern, date) is not None
print(f"{'egkiro ' if match else 'mi egkiro'} : { date}")

#Strong password validation
STRONG_PASSWORD_REGEX = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
for pwd in ["Password123!", "weakpass", "StrongPass1@", "NoSpecialChar1", "Short1!"]:
    ok = STRONG_PASSWORD_REGEX.fullmatch(pwd) is not None
    print(f"{'Έγκυρος' if ok else 'Μη έγκυρος'} κωδικός: {pwd}")