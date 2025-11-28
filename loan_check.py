import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# ---------------- Abstract Account Class ----------------
class Account(ABC):
    @abstractmethod
    def loan(self):
        pass

    def welcome(self):
        messagebox.showinfo("Welcome", "Checking if you are eligible for loan")


# ---------------- Form Validation ----------------
class FormValid:
    def __init__(self, name, age, gender, email, aadhar, pan_card, password, income):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.__aadhar = None
        self.__pan_card = None
        self._password = password
        self.valid = True

        self.aadhar_card = aadhar
        self.pan_card = pan_card
        self.password = password  

        # Validate email
        if not self.email.endswith("@gmail.com"):
            messagebox.showerror("Error", "Invalid Email ID")
            self.valid = False

        if self.valid:
            # Show entered info
            info = (
                f"Name      : {self.name}\n"
                f"Age       : {self.age}\n"
                f"Gender    : {self.gender}\n"
                f"Email     : {self.email}\n"
                f"Password  : {self._password}\n"
                f"Aadhar    : {self.__aadhar}\n"
                f"PAN Card  : {self.__pan_card}"
            )
            messagebox.showinfo("Form Info", info)

            acc = SaveAccount(self.name, self.age, income, self.email)
            acc.welcome()
            acc.loan()
        else:
            messagebox.showerror("Error", "Form is invalid. Cannot proceed.")

    @property
    def pan_card(self):
        return self.__pan_card

    @pan_card.setter
    def pan_card(self, pan_number):
        if len(pan_number) == 10 and pan_number[0].isalpha() and pan_number[-1].isalpha() and pan_number.isalnum():
            self.__pan_card = pan_number
        else:
            messagebox.showerror("Error", "Please enter a valid PAN card number")
            self.valid = False

    @property
    def aadhar_card(self):
        return self.__aadhar

    @aadhar_card.setter
    def aadhar_card(self, aadhar_num):
        if len(aadhar_num) == 12 and aadhar_num.isdigit():
            self.__aadhar = aadhar_num
        else:
            messagebox.showerror("Error", "Please enter a valid Aadhaar number")
            self.valid = False

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        digits = sum(c.isdigit() for c in pwd)
        ats = pwd.count("@")
        if len(pwd) == 8 and pwd[0].isupper() and digits >= 2 and ats == 1:
            self._password = pwd
        else:
            messagebox.showerror("Error", "Invalid Password")
            self.valid = False


# ---------------- Account Implementation ----------------
class SaveAccount(Account):
    def __init__(self, name, age, income, email_id):
        self.name = name
        self.age = age
        self.email_id = email_id
        self._income = income

    def loan(self):
        if 18 <= self.age <= 40:
            if self._income < 20000:
                messagebox.showinfo("Loan Result", "You are not eligible for a loan due to low income")
            elif 20000 <= self._income <= 70000:
                messagebox.showinfo("Loan Result", "You are eligible for a loan\nYou can take a loan of 7 lakh")
            else:
                messagebox.showinfo("Loan Result", "You are eligible for a loan\nAny amount of Loan can be taken")
        else:
            messagebox.showinfo("Loan Result", "You are not eligible for a loan due to age limit")


# ---------------- Tkinter GUI ----------------
def submit():
    try:
        name = entry_name.get()
        age = int(entry_age.get())
        gender = entry_gender.get()
        email = entry_email.get()
        aadhar = entry_aadhar.get()
        pan_card = entry_pan.get()
        password = entry_password.get()
        income = int(entry_income.get())
        FormValid(name, age, gender, email, aadhar, pan_card, password, income)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for age and income")


# Create main window
root = tk.Tk()
root.title("Loan Eligibility Form")
root.geometry("400x500")

# Labels and Entries
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Age").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Gender").pack()
entry_gender = tk.Entry(root)
entry_gender.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Aadhar").pack()
entry_aadhar = tk.Entry(root)
entry_aadhar.pack()

tk.Label(root, text="PAN Card").pack()
entry_pan = tk.Entry(root)
entry_pan.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Label(root, text="Income").pack()
entry_income = tk.Entry(root)
entry_income.pack()

tk.Button(root, text="Submit", command=submit).pack(pady=10)

# Run the GUI
root.mainloop()
