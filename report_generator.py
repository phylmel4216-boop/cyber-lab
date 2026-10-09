import os
from datetime import datetime

DATA_DIR = "data"
REPORT_FILE = os.path.join(DATA_DIR, "cyber_lab_report.txt")

FILES = [
    "system_info.txt",
    "network_info.txt",
    "integrity_results.txt",
    "password_results.txt",
]


def generate_report():
    os.makedirs(DATA_DIR, exist_ok=True)

    sections = [
        "========================================",
        "          CYBER LAB REPORT",
        "========================================",
        f"Generated: {datetime.now()}",
        "",
    ]

    for filename in FILES:
        path = os.path.join(DATA_DIR, filename)

        sections.append(f"\n--- {filename} ---\n")

        if os.path.isfile(path):
            with open(path, "r") as file:
                sections.append(file.read())
        else:
            sections.append("No results saved yet.\n")

    report = "\n".join(sections)

    with open(REPORT_FILE, "w") as file:
        file.write(report)

    print("\nReport generated successfully!")
    print("Saved to:", REPORT_FILE)


if __name__ == "__main__":
    generate_report()
