import os

TOOLS = {
    "System Information": "sysinfo.py",
    "Password Checker": "password_checker.py",
    "File Integrity Checker": "integrity_checker.py",
    "Network Information": "network_info.py",
    "Local Port Checker": "port_checker.py",
    "Report Generator": "report_generator.py",
}

print()
print("================================")
print("       CYBER LAB DASHBOARD")
print("================================")

for name, filename in TOOLS.items():
    if os.path.isfile(filename):
        status = "AVAILABLE"
    else:
        status = "MISSING"

    print(f"{name}: {status}")

print()
print("Dashboard check complete.")
