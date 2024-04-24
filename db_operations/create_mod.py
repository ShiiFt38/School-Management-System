from tkinter import messagebox
import sqlite3 as sq


class Create:
    def __init__(self, db):
        self.db = db

    def add_student(self, nr, fn, ln, e, g, a, ad, ctc, m, c):
        if nr and fn and ln and e and g and a and ad and ctc and m and c:
            try:
                self.db.add_student(nr, fn, ln, e, g, a, ad, ctc, m, c)

                messagebox.showinfo("Success", "Record added successfully.")

            except sq.IntegrityError:  # Built-in sqlite3 function to catch UNIQUE constraint violations
                messagebox.showerror("Error", f"Record for '{nr}' already exists.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def add_lecturer(self, nr, fn, ln, e, g, a):
        if nr and fn and ln and e and g and a:
            try:
                self.db.add_lecturer(nr, fn, ln, e, g, a)

                messagebox.showinfo("Success", "Record added successfully.")

            except sq.IntegrityError:
                messagebox.showerror("Error", f"Record for '{fn} {ln}' already exists.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
            print("Fill in all details")
