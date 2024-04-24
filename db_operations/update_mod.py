from tkinter import messagebox


class Update:
    def __init__(self, db):
        self.db = db

    def update_student(self, nr, fn, ln, e, g, a, ad, ctc, m, c):
        if self.db.entry_exists("students", nr):
            result = messagebox.askquestion("Confirmation",
                                            f"Are you sure you want update record with student number '{nr}'?")

            if result == 'yes' and nr and fn and ln and e and g and a and ad and ctc and m and c:
                self.db.update_student(fn, ln, e, g, a, ad, ctc, m, c, nr)

                messagebox.showinfo("Success", "Record updated successfully.")
            elif result == 'no':
                pass
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Enter an existing student number.")

    def update_lecturer(self, id, fn, ln, e, g, a):
        if self.db.entry_exists("lecturers", id):
            result = messagebox.askquestion("Confirmation",
                                            f"Are you sure you want to update the record with ID '{id}'?")

            if result == 'yes' and id and fn and ln and e and g and a:
                self.db.update_lecturer(fn, ln, e, g, a, id)

                messagebox.showinfo("Success", "Record updated successfully.")
            elif result == 'no':
                pass
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Enter an existing lecturer id")
