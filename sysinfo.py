import os
import platform

os.makedirs("data", exist_ok=True)

info = []

info.append("===== CYBER LAB SYSTEM INFORMATION =====")
info.append("")
info.append(f"Operating system: {platform.system()}")
info.append(f"Architecture: {platform.machine()}")
info.append(f"Python version: {platform.python_version()}")
info.append(f"Home directory: {os.getenv('HOME')}")

text = "\n".join(info)

print(text)

with open("data/system_info.txt", "w") as file:
    file.write(text + "\n")

print()
print("Saved to: data/system_info.txt")
