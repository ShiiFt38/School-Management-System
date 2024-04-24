from tkinter import messagebox


class Delete:
    def __init__(self, db):
        self.db = db

    def remove_student(self, id):
        if id and self.db.entry_exists("students", id):
            result = messagebox.askquestion("Confirmation",
                                            f"Are you sure you want to delete student record with ID '{id}'?")

            if result == 'yes':
                self.db.delete_student(id)
                messagebox.showinfo("Success", "Record deleted successfully.")
            else:
                pass
        else:
            messagebox.showerror("Error", "Enter an existing student number.")

    def remove_lecturer(self, id, lecturer, lname):
        if id and self.db.entry_exists("lecturers", id):
            result = messagebox.askquestion("Confirmation",
                                            f"Are you sure you want to delete {lecturer} {lname}'s record?")

            if result == 'yes':
                self.db.delete_lecturer(id)
                messagebox.showinfo("Success", "Record deleted successfully.")
            else:
                pass
        else:
            messagebox.showerror("Error", "Enter an existing identification number")