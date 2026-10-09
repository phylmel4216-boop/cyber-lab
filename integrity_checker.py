import hashlib
import os
from datetime import datetime

os.makedirs("data", exist_ok=True)

file_path = input("Enter the file path to check: ")

if not os.path.isfile(file_path):
    print("File not found. Check the path and try again.")
else:
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    file_hash = sha256.hexdigest()

    result = (
        "===== FILE INTEGRITY RESULT =====\n"
        f"Date: {datetime.now()}\n"
        f"File: {file_path}\n"
        f"SHA-256: {file_hash}\n"
        "=================================\n\n"
    )

    print()
    print(result)

    with open("data/integrity_results.txt", "a") as file:
        file.write(result)

    print("Result saved to: data/integrity_results.txt")
