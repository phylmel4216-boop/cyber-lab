import os
import sys
import socket
import platform
import hashlib
import string
from datetime import datetime

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView


class CyberLabApp(App):

    def build(self):
        self.title = "Cyber Lab"

        self.data_dir = os.path.join(
            self.user_data_dir, "data"
        )
        os.makedirs(self.data_dir, exist_ok=True)

        self.root_box = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        title = Label(
            text="[b]CYBER LAB[/b]\nMobile Security Toolkit",
            markup=True,
            font_size=dp(25),
            size_hint_y=None,
            height=dp(85)
        )

        self.root_box.add_widget(title)

        scroll = ScrollView()

        self.menu = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            size_hint_y=None
        )
        self.menu.bind(minimum_height=self.menu.setter("height"))

        buttons = [
            ("System Information", self.system_info),
            ("Password Strength", self.password_checker),
            ("File Integrity Checker", self.file_checker),
            ("Network Information", self.network_info),
            ("View Saved Reports", self.view_reports),
            ("About Cyber Lab", self.about),
        ]

        for text, action in buttons:
            button = Button(
                text=text,
                size_hint_y=None,
                height=dp(55),
                font_size=dp(16)
            )
            button.bind(on_release=action)
            self.menu.add_widget(button)

        scroll.add_widget(self.menu)
        self.root_box.add_widget(scroll)

        self.status = Label(
            text="Cyber Lab is ready.",
            size_hint_y=None,
            height=dp(35)
        )
        self.root_box.add_widget(self.status)

        return self.root_box

    def show_result(self, title, message):
        content = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(10)
        )

        scroll = ScrollView()

        result_label = Label(
            text=message,
            size_hint_y=None,
            halign="left",
            valign="top"
        )

        result_label.bind(
            width=lambda instance, width:
            setattr(instance, "text_size", (width, None))
        )
        result_label.bind(
            texture_size=lambda instance, size:
            setattr(instance, "height", size[1] + dp(20))
        )

        scroll.add_widget(result_label)
        content.add_widget(scroll)

        close_button = Button(
            text="Close",
            size_hint_y=None,
            height=dp(45)
        )
        content.add_widget(close_button)

        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.9, 0.8)
        )

        close_button.bind(on_release=popup.dismiss)
        popup.open()

    def system_info(self, instance):
        info = (
            "CYBER LAB - SYSTEM INFORMATION\n\n"
            f"Operating system: {platform.system()}\n"
            f"Architecture: {platform.machine()}\n"
            f"Python version: {platform.python_version()}\n"
            f"Device hostname: {socket.gethostname()}\n"
        )

        self.save_result("system_info.txt", info)
        self.show_result("System Information", info)
        self.status.text = "System information checked."

    def password_checker(self, instance):
        content = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(10)
        )

        password_input = TextInput(
            hint_text="Enter a test password",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=dp(50)
        )

        content.add_widget(password_input)

        check_button = Button(
            text="Check Strength",
            size_hint_y=None,
            height=dp(45)
        )
        content.add_widget(check_button)

        popup = Popup(
            title="Password Strength Checker",
            content=content,
            size_hint=(0.9, 0.4)
        )

        def check_password(instance):
            password = password_input.text
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

            result = (
                f"Strength: {strength}\n"
                f"Score: {score}/5\n"
                "Password stored: No"
            )

            self.save_result("password_results.txt", result)
            popup.dismiss()
            self.show_result("Password Result", result)

        check_button.bind(on_release=check_password)
        popup.open()

    def file_checker(self, instance):
        content = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(10)
        )

        path_input = TextInput(
            hint_text="Enter a file path accessible to the app",
            multiline=False,
            size_hint_y=None,
            height=dp(50)
        )

        content.add_widget(path_input)

        check_button = Button(
            text="Calculate SHA-256",
            size_hint_y=None,
            height=dp(45)
        )
        content.add_widget(check_button)

        popup = Popup(
            title="File Integrity Checker",
            content=content,
            size_hint=(0.9, 0.4)
        )

        def check_file(instance):
            path = path_input.text.strip()
            popup.dismiss()

            try:
                digest = hashlib.sha256()

                with open(path, "rb") as file:
                    for chunk in iter(
                        lambda: file.read(4096), b""
                    ):
                        digest.update(chunk)

                result = (
                    f"File: {path}\n\n"
                    f"SHA-256:\n{digest.hexdigest()}"
                )

                self.save_result("integrity_results.txt", result)
                self.show_result("File Integrity Result", result)

            except (OSError, ValueError) as error:
                self.show_result(
                    "File Error",
                    f"Could not read the file.\n{error}"
                )

        check_button.bind(on_release=check_file)
        popup.open()

    def network_info(self, instance):
        hostname = socket.gethostname()

        try:
            local_ip = socket.gethostbyname(hostname)
        except OSError:
            local_ip = "Unavailable"

        info = (
            "NETWORK INFORMATION\n\n"
            f"Hostname: {hostname}\n"
            f"Local IP: {local_ip}\n\n"
            "This shows basic device network information."
        )

        self.save_result("network_info.txt", info)
        self.show_result("Network Information", info)

    def view_reports(self, instance):
        files = []

        for filename in os.listdir(self.data_dir):
            if filename.endswith(".txt"):
                files.append(filename)

        if not files:
            self.show_result("Saved Reports", "No reports yet.")
            return

        reports = []

        for filename in sorted(files):
            path = os.path.join(self.data_dir, filename)

            try:
                with open(path, "r") as file:
                    reports.append(
                        f"===== {filename} =====\n{file.read()}"
                    )
            except OSError:
                continue

        self.show_result(
            "Saved Reports",
            "\n\n".join(reports)
        )

    def save_result(self, filename, text):
        path = os.path.join(self.data_dir, filename)

        with open(path, "a") as file:
            file.write(
                f"Date: {datetime.now()}\n"
                f"{text}\n"
                "------------------------------\n"
            )

    def about(self, instance):
        self.show_result(
            "About Cyber Lab",
            "Cyber Lab Mobile\n"
            "Version 1.0\n\n"
            "A Python-based learning toolkit for "
            "basic system information, password "
            "strength checks, file hashes, and "
            "network information."
        )


if __name__ == "__main__":
    CyberLabApp().run()
