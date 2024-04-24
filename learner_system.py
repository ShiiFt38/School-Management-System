import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from db_operations.read_mod import Read
from db_operations.delete_mod import Delete
from db_operations.update_mod import Update
from db_operations.create_mod import Create

# Learner management system's class, widgets and functions
class LearnerManagementWindow:
    def __init__(self, master, db):
        self.master = master        # tkinter root
        self.db = db                # Stores the Database class instance
        self.master.title("Learner Management Window")
        self.master.geometry("1350x700")

        # Configuring the column span of the window
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=5)

        # Configuring the row span of the window
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=3)

        # Frame for holding the title label
        self.title_frame = tk.Frame(master, bg="#1b1b21")
        self.title_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

        # Primary heading for the window
        self.page_title = tk.Label(self.title_frame, text="Student Management", font=("Arial", 30, "bold"), border=12, bg="#1b1b21", fg="#ffffff")
        self.page_title.pack(fill=tk.BOTH, expand=True)


        # Frame containing form for student details
        self.student_info_frame = tk.LabelFrame(master, text="Student Details", font=("Arial", 15, 'bold'), fg="#48c4c4")
        self.student_info_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        self.details_widgets()

        # Frame for listbox showing data
        self.dataFrame = tk.LabelFrame(master, text="Students Information", font=("Arial", 15, 'bold'), fg="#48c4c4")
        self.dataFrame.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')
        self.info_widgets()
        self.populate_treeview()

        # Frame for button widgets
        self.actionFrame = tk.LabelFrame(self.student_info_frame, bg='#ffffff')
        self.actionFrame.grid(row=11, column=0, columnspan=3, pady=20)
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

        self.delete_btn = tk.Button(self.actionFrame, text="Delete" ,command=self.delete_data, bg="#e23c2c")
        self.delete_btn.grid(row=0, column=3, padx=20, pady=10)

        self.exit_btn = tk.Button(self.student_info_frame, text="Exit", command=self.exit_window, bg="#9b9a98", fg="#ffffff", padx=30, pady=5, font=("Arial", 10, 'bold'))
        self.exit_btn.grid(row=12, column=0, columnspan=3, pady=20)

        for widget in self.actionFrame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

    # Widgets for student details form
    def details_widgets(self):

        #Student number textbox
        self.St_nr = tk.StringVar()
        self.student_nr = tk.Label(self.student_info_frame, text="Student Number: ")
        self.St_nr_txtbox = tk.Entry(self.student_info_frame, textvariable=self.St_nr)
        self.student_nr.grid(row=1, column=0)
        self.St_nr_txtbox.grid(row=1, column=1)

        #First name textbox
        self.firstName = tk.StringVar()
        self.firstName_lbl = tk.Label(self.student_info_frame, text="First name: ")
        self.firstName_txtbox = tk.Entry(self.student_info_frame, textvariable=self.firstName)
        self.firstName_lbl.grid(row=2, column=0)
        self.firstName_txtbox.grid(row=2, column=1)

        #Last name textbox
        self.lastName = tk.StringVar()
        self.lastName_lbl = tk.Label(self.student_info_frame, text="Last Name: ")
        self.lastName_txtbox = tk.Entry(self.student_info_frame, textvariable=self.lastName)
        self.lastName_lbl.grid(row=3, column=0)
        self.lastName_txtbox.grid(row=3, column=1)

        #Email textbox
        self.StEmail = tk.StringVar()
        self.StEmail_lbl = tk.Label(self.student_info_frame, text="Email: ")
        self.StEmail_txtbox = tk.Entry(self.student_info_frame, textvariable=self.StEmail)
        self.StEmail_lbl.grid(row=4, column=0)
        self.StEmail_txtbox.grid(row=4, column=1)

        #Gender textbox
        self.gender = tk.StringVar()
        self.gender_lbl = tk.Label(self.student_info_frame, text="Gender: ")
        self.gender_txtbox = ttk.Combobox(self.student_info_frame, values=[' ', 'Male', 'Female'], textvariable=self.gender)
        self.gender_lbl.grid(row=5, column=0)
        self.gender_txtbox.grid(row=5, column=1)

        #Age textbox
        self.Age = tk.StringVar()
        self.age_lbl = tk.Label(self.student_info_frame, text="Age: ")
        self.age_txtbox = tk.Spinbox(self.student_info_frame, from_=18, to=35, textvariable=self.Age)
        self.age_lbl.grid(row=6, column=0)
        self.age_txtbox.grid(row=6, column=1)


        #Address textbox
        self.Address = tk.StringVar()
        self.address_lbl = tk.Label(self.student_info_frame, text="Address: ")
        self.address_txtbox = tk.Entry(self.student_info_frame, textvariable=self.Address)
        self.address_lbl.grid(row=7, column=0)
        self.address_txtbox.grid(row=7, column=1)

        #Contact textbox
        self.Contact = tk.StringVar()
        self.contact_lbl = tk.Label(self.student_info_frame, text="Contact: ")
        self.contact_txtbox = tk.Entry(self.student_info_frame, textvariable=self.Contact)
        self.contact_lbl.grid(row=8, column=0)
        self.contact_txtbox.grid(row=8, column=1)

        #Course Mode combo box
        self.Mode = tk.StringVar()
        self.courseMode_lbl = tk.Label(self.student_info_frame, text="Course Mode: ")
        self.courseMode_Combobox = ttk.Combobox(self.student_info_frame, values=['', 'Full-Time', 'Part-Time'], textvariable=self.Mode)
        self.courseMode_lbl.grid(row=9, column=0)
        self.courseMode_Combobox.grid(row=9, column=1)
        self.courseMode_Combobox.bind("<<ComboboxSelected>>", self.course_option)

        #Course combo box
        self.Course = tk.StringVar()
        self.course_lbl = tk.Label(self.student_info_frame, text="Course: ")
        self.course_combobox = ttk.Combobox(self.student_info_frame, textvariable=self.Course)
        self.course_lbl.grid(row=10, column=0)
        self.course_combobox.grid(row=10, column=1)

        for widget in self.student_info_frame.winfo_children():
            widget.grid_configure(padx=20, pady=10)

    # Widgets for student information frame
    def info_widgets(self):
        # Search box
        self.search_item = tk.StringVar()
        self.search_txtbox = tk.Entry(self.dataFrame, textvariable=self.search_item, width=30)
        self.search_btn = tk.Button(self.dataFrame, text="Search", command=self.search_entry)
        self.search_txtbox.pack(pady=5)
        self.search_btn.pack(pady=5)

        # Treeview columns
        self.columns = ("ID", "First Name", "Last Name", "Email", "Gender",
                        "Age", "Address", "Contact", "Course Mode", "Course")
        self.student_treeview = ttk.Treeview(self.dataFrame, columns=self.columns, show='headings')
        self.student_treeview.pack(fill=tk.BOTH, expand=True)
        self.student_treeview.bind("<<TreeviewSelect>>", self.on_select)

        # Scrollbars
        self.tree_scroll_y = ttk.Scrollbar(self.dataFrame, orient='vertical', command=self.student_treeview.yview)
        self.tree_scroll_y.pack(side='right', fill='y')
        self.tree_scroll_x = ttk.Scrollbar(self.dataFrame, orient='horizontal', command=self.student_treeview.xview)
        self.tree_scroll_x.pack(side='bottom', fill='x')

        self.student_treeview.config(yscrollcommand=self.tree_scroll_y.set, xscrollcommand=self.tree_scroll_x.set)

        # Column Heading Names
        self.student_treeview.heading("ID", text="ID")
        self.student_treeview.heading("First Name", text="First Name")
        self.student_treeview.heading("Last Name", text="Last Name")
        self.student_treeview.heading("Email", text="Email")
        self.student_treeview.heading("Gender", text="Gender")
        self.student_treeview.heading("Age", text="Age")
        self.student_treeview.heading("Address", text="Address")
        self.student_treeview.heading("Contact", text="Contact")
        self.student_treeview.heading("Course Mode", text="Mode")
        self.student_treeview.heading("Course", text="Course")

        self.refresh_btn = tk.Button(self.dataFrame, text="Refresh", command=self.populate_treeview)
        self.refresh_btn.pack(pady=5)

        # Treeview Column configurations
        for col in self.columns:
            self.student_treeview.column(col, width=100, minwidth=50)  # Set initial width for columns
            self.student_treeview.heading(col, text=col, anchor='center')  # Center align column headers

    # Function for dynamic course selection limitations
    def course_option(self, event=None):
        selected_mode = self.courseMode_Combobox.get()

        # Conditional statement to change available course depending on course mode
        if selected_mode == 'Full-Time':
            courses = ['Bachelor of Computing', 'Bachelor of IT',
                       'Diploma in IT', 'Diploma for Deaf Students',
                       'Certificate: IT', 'National Certificate: IT']
        elif selected_mode == 'Part-Time':
            courses = ['Bachelor of IT']
        else:
            courses = []

        self.course_combobox['values'] = courses

    # Function to clear form entries
    def clear_entry(self):
        self.firstName.set("")
        self.lastName.set("")
        self.St_nr.set("")
        self.StEmail.set("")
        self.gender.set("")
        self.Age.set("")
        self.Address.set("")
        self.Contact.set("")
        self.Mode.set("")
        self.Course.set("")

    # Function to fetch data and populate treeview
    def populate_treeview(self):
        Read(self.db).populate_treeview(self.search_item, self.student_treeview, "students")

    # Function to get data from treeview and pass to form entries
    def on_select(self, event=None):
        # Treeview event to get selected item
        selected_item = self.student_treeview.focus()

        values = self.student_treeview.item(selected_item, "values")

        # Conditional statement to avoid attempting to get values when nothing is selected
        if values and len(values) >= 10:
            self.St_nr.set(values[0])
            self.firstName.set(values[1])
            self.lastName.set(values[2])
            self.StEmail.set(values[3])
            self.gender.set(values[4])
            self.Age.set(values[5])
            self.Address.set(values[6])
            self.Contact.set(values[7])
            self.Mode.set(values[8])
            self.Course.set(values[9])
        else:
            # Handles cases where values are empty or don't have enough elements
            self.St_nr.set("")
            self.firstName.set("")
            self.lastName.set("")
            self.StEmail.set("")
            self.gender.set("")
            self.Age.set("")
            self.Address.set("")
            self.Contact.set("")
            self.Mode.set("")
            self.Course.set("")

    # Function to add records to database
    def add_data(self):
        student_nr = self.St_nr_txtbox.get()
        firstname = self.firstName_txtbox.get()
        lastname = self.lastName_txtbox.get()
        email = self.StEmail_txtbox.get()
        gender = self.gender_txtbox.get()
        age = self.age_txtbox.get()
        address = self.address_txtbox.get()
        contact = self.contact_txtbox.get()
        mode = self.courseMode_Combobox.get()
        course = self.course_combobox.get()

        Create(self.db).add_student(student_nr, firstname, lastname, email, gender, age, address, contact, mode, course)

    # Function to delete record from database
    def delete_data(self):
        student_nr = self.St_nr.get()
        Delete(self.db).remove_student(student_nr)

    # Function to update record in database
    def update_data(self):
        student_nr = self.St_nr_txtbox.get()
        firstname = self.firstName_txtbox.get()
        lastname = self.lastName_txtbox.get()
        email = self.StEmail_txtbox.get()
        gender = self.gender_txtbox.get()
        age = self.age_txtbox.get()
        address = self.address_txtbox.get()
        contact = self.contact_txtbox.get()
        mode = self.courseMode_Combobox.get()
        course = self.course_combobox.get()

        Update(self.db).update_student(student_nr, firstname, lastname, email, gender, age, address, contact, mode, course)

    # Function for search button
    def search_entry(self):
        Read(self.db).search_entry(self.search_item, self.student_treeview, "students")

    # Function to exit window
    def exit_window(self):
        result = messagebox.askquestion('Confirmation', "Are you sure you want to close this window?")
        if result == 'yes':
            self.master.destroy()
        else:
            pass


