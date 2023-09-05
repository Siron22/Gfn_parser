import os
import time
import tkinter as tk
from tkinter import messagebox
from start_page import GfnParser
from configparser import ConfigParser

from utilities import get_root_directory


class GfnParserApp:
    def __init__(self, root, gfn_parser: GfnParser):
        self.password_entry = None
        self.email_entry = None
        self.root = root
        self.gfn_parser = gfn_parser
        self.root.title("GFN Study time manager")
        self.root.geometry("600x300")

        self.create_widgets()

        self.config_path = os.path.join(get_root_directory(), 'config.ini')
        self.config = ConfigParser()
        self._load_credentials()

    def _save_credentials(self):

        self.config['Credentials'] = {
            'email': self.email_entry.get(),
            'password': self.password_entry.get()
        }

        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def _load_credentials(self):

        self.config.read(self.config_path)

        if 'Credentials' in self.config:
            credentials = self.config['Credentials']
            if 'email' in credentials and 'password' in credentials:
                self.email_entry.insert(0, credentials['email'])
                self.password_entry.insert(0, credentials['password'])

    def _delete_credentials(self):
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self._save_credentials()  # Save an empty entry to overwrite previous credentials

    def start_count(self):
        self._save_credentials()
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.gfn_parser.start_time(email, password)
        # self.gfn_parser.navigate_to_main()

    def stop_count(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not email or not password:
            tk.messagebox.showerror("Error", "Please enter both email and password.")
            return
        self._save_credentials()
        self.gfn_parser.end_time(email, password)

    def create_widgets(self):
        self.root.configure(background='lightblue')

        self.create_title_label()
        self.create_email_widgets()
        self.create_password_widgets()
        self.create_action_buttons()

    def create_title_label(self):
        label = tk.Label(self.root, text="GFN Study Time Manager", font=("Times New Roman", 20, "bold"))
        label.pack()

    def create_email_widgets(self):
        email_label = tk.Label(self.root, text="Email:", font=("Times New Roman", 16))
        self.email_entry = tk.Entry(self.root, bg="lightyellow", font=("Times New Roman", 14))
        email_label.pack()
        self.email_entry.pack()

    def create_password_widgets(self):
        password_label = tk.Label(self.root, text="Password:", font=("Times New Roman", 16))
        self.password_entry = tk.Entry(self.root, show="*", bg="lightyellow", font=("Times New Roman", 14))
        password_label.pack()
        self.password_entry.pack()

    def create_action_buttons(self):
        action_frame = tk.Frame(self.root)
        action_frame.pack()

        start_button = tk.Button(action_frame, text="Start", command=self.start_count,
                                 font=("Times New Roman", 16, "bold"), bg="tan")
        stop_button = tk.Button(action_frame, text="Stop", command=self.stop_count,
                                font=("Times New Roman", 16, "bold"), bg="tan")
        delete_button = tk.Button(self.root, text="Delete Credentials", command=self._delete_credentials,
                                  font=("Times New Roman", 16, "bold"), bg="tan")

        # Place buttons on the right side
        stop_button.pack(side=tk.RIGHT)
        start_button.pack(side=tk.RIGHT)
        delete_button.pack(side=tk.RIGHT)


