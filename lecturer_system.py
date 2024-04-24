import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


# Learner management system's class, widgets and functions
class LecturerManagementWindow:
    def __init__(self, master, db):
        self.master = master        # tkinter root
        self.db = db                # Stores the Database class instance
        self.master.title("Lecturer Management Window")
        self.master.geometry("1350x600")

        # Configuring the column span of the window
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=5)

        # Configuring the row span of the window
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=5)

        # Frame for holding the title label
        self.title_frame = tk.Frame(master, bg="#1b1b21")
        self.title_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

        # Window Title
        self.lecturer_label = tk.Label(self.title_frame, text="Lecturer Management", font=("Arial", 30, "bold"), border=12, bg="#1b1b21", fg="#ffffff")
        self.lecturer_label.pack(fill=tk.BOTH, expand=True)

        # Frame for lecturer data input
        self.lecturer_info_frame = tk.LabelFrame(master, text="Lecturer Details", font=("Arial", 15, 'bold'), fg="#48c4c4")
        self.lecturer_info_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        self.details_widgets()

        # Frame for lecturer listbox
        self.listFrame = tk.LabelFrame(master, text="Lecturers' Information", font=("Arial", 15, 'bold'), fg="#48c4c4")
        self.listFrame.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')
        self.info_widgets()
        self.populate_treeview()

        # Frame for button widgets
        self.actionFrame = tk.LabelFrame(self.lecturer_info_frame, bg='#ffffff')
        self.actionFrame.grid(row=6, column=0, columnspan=3, pady=20)
        self.actionFrame.grid_columnconfigure(0, weight=1)
        self.action_buttons()

    # Buttons for CRUD operations
    def action_buttons(self):
        self.add_btn = tk.Button(self.actionFrame, text="Submit", command=self.add_data)
        self.add_btn.grid(row=0, column=0, padx=20, pady=10)

        self.update_btn = tk.Button(self.actionFrame, text="Update", command=self.update_data)
        self.update_btn.grid(row=0, column=1, padx=20, pady=10)

        self.clear_btn = tk.Button(self.actionFrame, text="Clear", command=self.clear_entry)
        self.clear_btn.grid(row=0, column=2, padx=20, pady=10)

        self.delete_btn = tk.Button(self.actionFrame, text="Delete", command=self.delete_data, bg="#e23c2c")
        self.delete_btn.grid(row=0, column=3, padx=20, pady=10)

        self.exit_btn = tk.Button(self.lecturer_info_frame, text="Exit", command=self.exit_window, bg="#9b9a98", fg="#ffffff", padx=30, pady=5)
        self.exit_btn.grid(row=7, column=0, columnspan=3, pady=20)

        for widget in self.actionFrame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

    # Widgets for lecturer details form
    def details_widgets(self):
        self.lecturer_id = tk.StringVar()
        self.id_label = tk.Label(self.lecturer_info_frame, text="Identification Number: ")
        self.id_txtbox = tk.Entry(self.lecturer_info_frame, textvariable=self.lecturer_id)
        self.id_label.grid(row=0, column=0)
        self.id_txtbox.grid(row=0, column=1)

        self.Firstname = tk.StringVar()
        self.firstName_lbl = tk.Label(self.lecturer_info_frame, text="First name: ")
        self.firstName_txtbox = tk.Entry(self.lecturer_info_frame, textvariable=self.Firstname)
        self.firstName_lbl.grid(row=1, column=0)
        self.firstName_txtbox.grid(row=1, column=1)

        self.Lastname = tk.StringVar()
        self.lastName_lbl = tk.Label(self.lecturer_info_frame, text="Last Name: ")
        self.lastName_txtbox = tk.Entry(self.lecturer_info_frame, textvariable=self.Lastname)
        self.lastName_lbl.grid(row=2, column=0)
        self.lastName_txtbox.grid(row=2, column=1)

        self.Email = tk.StringVar()
        self.Email_lbl = tk.Label(self.lecturer_info_frame, text="Email: ")
        self.Email_txtbox = tk.Entry(self.lecturer_info_frame, textvariable=self.Email)
        self.Email_lbl.grid(row=3, column=0)
        self.Email_txtbox.grid(row=3, column=1)

        self.Gender = tk.StringVar()
        self.gender_lbl = tk.Label(self.lecturer_info_frame, text="Gender: ")
        self.gender_txtbox = ttk.Combobox(self.lecturer_info_frame, values=[' ', 'Male', 'Female'],
                                          textvariable=self.Gender)
        self.gender_lbl.grid(row=4, column=0)
        self.gender_txtbox.grid(row=4, column=1)

        self.Age = tk.StringVar()
        self.age_lbl = tk.Label(self.lecturer_info_frame, text="Age: ")
        self.age_txtbox = tk.Spinbox(self.lecturer_info_frame, from_=18, to=55, textvariable=self.Age)
        self.age_lbl.grid(row=5, column=0)
        self.age_txtbox.grid(row=5, column=1)

        for widget in self.lecturer_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

    # Widgets for student information frame
    def info_widgets(self):
        self.search_item = tk.StringVar()
        self.search_txtbox = tk.Entry(self.listFrame, textvariable=self.search_item, width=30)
        self.search_btn = tk.Button(self.listFrame, text="Search", command=self.search_entry)
        self.search_txtbox.pack(pady=5)
        self.search_btn.pack(pady=5)

        self.columns = ("ID", "First Name", "Last Name", "Email", "Gender", "Age")
        self.lecturer_treeview = ttk.Treeview(self.listFrame, columns=self.columns, show='headings')
        self.lecturer_treeview.bind("<<TreeviewSelect>>", self.on_select)

        # Adding Scrollbars
        self.tree_scroll_y = ttk.Scrollbar(self.listFrame, orient='vertical', command=self.lecturer_treeview.yview)
        self.tree_scroll_y.pack(side='right', fill='y')
        self.tree_scroll_x = ttk.Scrollbar(self.listFrame, orient='horizontal', command=self.lecturer_treeview.xview)
        self.tree_scroll_x.pack(side='bottom', fill='x')

        self.lecturer_treeview.config(yscrollcommand=self.tree_scroll_y.set, xscrollcommand=self.tree_scroll_x.set)

        self.lecturer_treeview.heading('ID', text='ID')
        self.lecturer_treeview.heading('First Name', text='First Name')
        self.lecturer_treeview.heading('Last Name', text='Surname')
        self.lecturer_treeview.heading('Email', text='Email')
        self.lecturer_treeview.heading('Gender', text='Gender')
        self.lecturer_treeview.heading('Age', text='Age')
        self.lecturer_treeview.pack(fill=tk.BOTH, expand=True)

        self.refresh_btn = tk.Button(self.listFrame, text="Refresh", command=self.populate_treeview)
        self.refresh_btn.pack(pady=5)

        # Adjust column weights for Treeview
        for col in self.columns:
            self.lecturer_treeview.column(col, width=150, minwidth=100)  # Set initial width for columns
            self.lecturer_treeview.heading(col, text=col, anchor='center')  # Center align column headers

    # Function to clear form entries
    def clear_entry(self):
        self.lecturer_id.set("")
        self.Firstname.set("")
        self.Lastname.set("")
        self.Email.set("")
        self.Gender.set("")
        self.Age.set("")

    # Function to fetch data and populate treeview
    def populate_treeview(self):
        self.search_item.set("")
        # Clear existing data in the Treeview
        self.lecturer_treeview.delete(*self.lecturer_treeview.get_children())

        if self.db.fetch_data("lecturers"):
            for row in self.db.fetch_data("lecturers"):
                self.lecturer_treeview.insert("", "end", values=row)
        else:
            print("Could not fetch data.")

    # Function to add records to database
    def add_data(self):
        lecturer_id = self.id_txtbox.get()
        firstname = self.firstName_txtbox.get()
        lastname = self.lastName_txtbox.get()
        email = self.Email_txtbox.get()
        gender = self.gender_txtbox.get()
        age = self.age_txtbox.get()

        if lecturer_id and firstname and lastname and email and gender and age:
            try:
                self.db.add_lecturer(lecturer_id, firstname, lastname, email, gender, age)

                messagebox.showinfo("Success", "Form submitted successfully.")
                self.clear_entry()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", f"Record for '{firstname} {lastname}' already exists.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
            print("Fill in all details")

    # Function to get data from treeview and pass to form entries
    def on_select(self, event):
        selected_item = self.lecturer_treeview.focus()

        values = self.lecturer_treeview.item(selected_item, "values")

        if values and len(values) >= 10:
            self.lecturer_id.set(values[0])
            self.Firstname.set(values[1])
            self.Lastname.set(values[2])
            self.Email.set(values[3])
            self.Gender.set(values[4])
            self.Age.set(values[5])
        else:
            self.lecturer_id.set("")
            self.Firstname.set("")
            self.Lastname.set("")
            self.Email.set("")
            self.Gender.set("")
            self.Age.set("")

    # Function to delete record from database
    def delete_data(self):
        lecturer_id = self.lecturer_id.get()
        lecturer = self.Firstname.get()
        surname = self.Lastname.get()

        if lecturer_id and self.db.entry_exists("lecturers", lecturer_id):
            result = messagebox.askquestion("Confirmation",
                                            f"Are you sure you want to delete {lecturer} {surname}'s record?")

            if result == 'yes':
                self.db.delete_lecturer(lecturer_id)
                messagebox.showinfo("Success", "Record deleted successfully.")
            else:
                pass
        else:
            messagebox.showerror("Error", "Enter an existing identification number")

    # Function to update record in database
    def update_data(self):
        lecturer_id = self.id_txtbox.get()
        firstname = self.firstName_txtbox.get()
        lastname = self.lastName_txtbox.get()
        email = self.Email_txtbox.get()
        gender = self.gender_txtbox.get()
        age = self.age_txtbox.get()

        if self.db.entry_exists("lecturers", lecturer_id):
            result = messagebox.askquestion("Confirmation", f"Are you sure you want to update the record with ID '{lecturer_id}'?")

            if result == 'yes' and lecturer_id and firstname and lastname and email and gender and age:
                self.db.update_lecturer(firstname, lastname, email, gender, age, lecturer_id)

                self.clear_entry()
                messagebox.showinfo("Success", "Record updated successfully.")
            elif result == 'no':
                pass
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Enter an existing lecturer id")

    # Function for search button
    def search_entry(self):
        search_item = self.search_item.get()

        for record in self.lecturer_treeview.get_children():
            self.lecturer_treeview.delete(record)

        if self.db.search("lecturers", search_item):
            for row in self.db.search("lecturers", search_item):
                self.lecturer_treeview.insert("", "end", values=row)
        else:
            messagebox.showerror("Error", f"'{search_item}' not found.")

    # Function to exit window
    def exit_window(self):
        result = messagebox.askquestion('Confirmation', "Are you sure you want to close this window?")
        if result == 'yes':
            self.master.destroy()
        else:
            pass
