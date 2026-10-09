import os
import platform

print("===== CYBER TOOL =====")
print()

print("Operating system:", platform.system())
print("Architecture:", platform.machine())
print("Python version:", platform.python_version())
print("Current user:", os.getenv("USER"))
print("Home directory:", os.getenv("HOME"))

print()
print("===== DONE =====")
