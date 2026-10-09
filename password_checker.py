import string
import os
from datetime import datetime

os.makedirs("data", exist_ok=True)

password = input("Enter a test password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c in string.punctuation for c in password):
    score += 1

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print()
print("Password strength:", strength)

result = (
    f"Date: {datetime.now()}\n"
    f"Strength: {strength}\n"
    f"Score: {score}/5\n"
    "Password stored: No\n"
    "------------------------------\n"
)

with open("data/password_results.txt", "a") as file:
    file.write(result)

print("Result saved to: data/password_results.txt")
