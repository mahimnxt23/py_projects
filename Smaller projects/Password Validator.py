"""It's a challange of creating a Password Validator. And the conditions are,
#1. It has to be done using Regular Expressions,
#2. The password should be at least 8 characters long,
#3. It can contain any letter, number and only [@#$%] <-- these symbols,
#4. It has to end with a number.
 
So, Let's begin....."""

import re

pattern = re.compile(r"[A-Za-z0-9@#$%]{7,}\d")   #{x,} is a way of limiting the length of the string

user_input = input('Enter your password:   ')

check = pattern.search(user_input)

print(check)