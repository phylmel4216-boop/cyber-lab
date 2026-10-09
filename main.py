import subprocess
import sys
import os

while True:
    print("\n===== CYBER LAB =====")
    print("1. System Information")
    print("2. Password Checker")
    print("3. File Integrity Checker")
    print("4. Network Information")
    print("5. Local Port Checker")
    print("6. Generate Report")
    print("7. Tools Dashboard")
    print("8. Exit")

    choice = input("Choose an option: ")

    tools = {
        "1": "sysinfo.py",
        "2": "password_checker.py",
        "3": "integrity_checker.py",
        "4": "network_info.py",
        "5": "port_checker.py",
        "6": "report_generator.py",
        "7": "dashboard.py"
    }

    if choice == "8":
        print("Goodbye, bro!")
        break

    elif choice in tools:
        filename = tools[choice]

        if os.path.isfile(filename):
            subprocess.run([sys.executable, filename])
        else:
            print("Tool not found:", filename)

    else:
        print("Invalid choice.")

    input("Press Enter to continue...")
