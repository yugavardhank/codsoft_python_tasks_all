import tkinter as tk
from tkinter import messagebox
import json
import os

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.filename = "contacts.json"
        self.contacts = self.load_contacts()

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack()

        self.address_entry = tk.Entry(root)
        self.address_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        self.save_contacts()
        messagebox.showinfo("Contact Added", f"Contact {name} added.")
        self.clear_entries()

    def view_contacts(self):
        if self.contacts:
            contacts_str = "\n".join([f'{name}: {details}' for name, details in self.contacts.items()])
            messagebox.showinfo("Contacts", contacts_str)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            details = self.contacts[name]
            messagebox.showinfo("Contact Found", f'{name}: {details}')
        else:
            messagebox.showerror("Error", f"No contact found with the name {name}.")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            self.save_contacts()
            messagebox.showinfo("Contact Updated", f"Contact {name} updated.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"No contact found with the name {name}.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            messagebox.showinfo("Contact Deleted", f"Contact {name} deleted.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"No contact found with the name {name}.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Usage
root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()