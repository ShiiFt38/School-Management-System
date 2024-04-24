import tkinter as tk
from db import Database
from learner_system import LearnerManagementWindow
from lecturer_system import LecturerManagementWindow


class mainWindow:
    def __init__(self, master):
        self.master = master        # tkinter root
        self.master.title("School Management System")
        self.master.geometry("800x500")

        self.db = Database("management_system.db")

        # Frame for main window's title label
        self.title_frame = tk.Frame(master, bg="#48c4c4")
        self.title_frame.pack(fill=tk.X)

        # Title label
        self.main_title = tk.Label(self.title_frame, text="School Management", font=("Arial", 30, "bold"), border=12, bg="#48c4c4")
        self.main_title.pack(pady=20)

        # Button for opening learner management window
        self.btn_learner = tk.Button(self.master, text="Learner Management", command=self.open_learner_window, pady=20, padx=25, bg="#b92a65",
                                     font=("Arial", 15), border=6, fg="#ffffff")
        self.btn_learner.pack(padx=20, pady=(40, 20))

        # Button for opening lecturer management window
        self.btn_lecturer = tk.Button(self.master, text="Lecturer Management", command=self.open_lecturer_window, pady=20, padx=25, bg="#b92a65",
                                      font=("Arial", 15), border=6, fg="#ffffff")
        self.btn_lecturer.pack(padx=10, pady=20)

    def open_learner_window(self):
        self.master.iconify()           # Minimizes the main window before opening child window
        self.learner_window = tk.Toplevel(self.master)      # Indicates new window
        self.learner_app = LearnerManagementWindow(self.learner_window, self.db)     # New window based on Learner management class
        self.learner_window.lift()

    def open_lecturer_window(self):
        self.master.iconify()           # Minimizes the main window before opening child window
        self.lecturer_window = tk.Toplevel(self.master)     # Indicates new window
        self.lecturer_app = LecturerManagementWindow(self.lecturer_window, self.db)     # New window based on Lecturer management class
        self.lecturer_window.lift()


def main():
    root = tk.Tk()
    app = mainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
