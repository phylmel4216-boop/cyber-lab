import hashlib
import os

file_path = input("Enter the file path: ")

if not os.path.isfile(file_path):
    print("File not found.")
else:
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    print()
    print("File:", file_path)
    print("SHA-256:", sha256.hexdigest())
