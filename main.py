import subprocess
from datetime import datetime
import os

LOG_FILE = "data/activity.log"


def log_activity(message):
    os.makedirs("data", exist_ok=True)

    with open(LOG_FILE, "a") as log:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{time}] {message}\n")


while True:
    print()
    print("==============================")
    print("       CYBER LAB v1.1")
    print("==============================")
    print("1. System Information")
    print("2. Password Strength Checker")
    print("3. File Integrity Checker")
    print("4. Network Information")
    print("5. Local Port Checker")
    print("6. View Activity Log")
    print("7. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        log_activity("System Information started")
        subprocess.run(["python", "sysinfo.py"])

    elif choice == "2":
        log_activity("Password Strength Checker started")
        subprocess.run(["python", "password_checker.py"])

    elif choice == "3":
        log_activity("File Integrity Checker started")
        subprocess.run(["python", "integrity_checker.py"])

    elif choice == "4":
        log_activity("Network Information started")
        subprocess.run(["python", "network_info.py"])

    elif choice == "5":
        log_activity("Local Port Checker started")
        subprocess.run(["python", "port_checker.py"])

    elif choice == "6":
        print("\n===== ACTIVITY LOG =====")

        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as log:
                content = log.read()

            if content:
                print(content)
            else:
                print("No activity recorded yet.")
        else:
            print("No activity recorded yet.")

    elif choice == "7":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice.")

    input("\nPress Enter to return to the menu...")
