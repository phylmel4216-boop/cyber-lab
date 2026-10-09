import subprocess

while True:
    print()
    print("==============================")
    print("       CYBER LAB v1.0")
    print("==============================")
    print("1. System Information")
    print("2. Password Strength Checker")
    print("3. File Integrity Checker")
    print("4. Network Information")
    print("5. Local Port Checker")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        subprocess.run(["python", "sysinfo.py"])

    elif choice == "2":
        subprocess.run(["python", "password_checker.py"])

    elif choice == "3":
        subprocess.run(["python", "integrity_checker.py"])

    elif choice == "4":
        subprocess.run(["python", "network_info.py"])

    elif choice == "5":
        subprocess.run(["python", "port_checker.py"])

    elif choice == "6":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice.")

    input("\nPress Enter to return to the menu...")
