import sqlite3 as sq


class Database:
    def __init__(self, db):
        self.connection = sq.connect(db)
        self.cursor = self.connection.cursor()

        create_student_table = ("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, "
                                "st_name TEXT, st_lastname TEXT, st_email TEXT, gender TEXT,"
                                "age INTEGER, address TEXT, contact TEXT, courseMode TEXT, course TEXT)")

        create_lecturer_table = ("CREATE TABLE IF NOT EXISTS lecturers (id INTEGER PRIMARY KEY, "
                                 "lt_name TEXT, lt_lastname TEXT, lt_email TEXT, gender TEXT, age INTEGER)")

        self.cursor.execute(create_student_table)
        self.cursor.execute(create_lecturer_table)

        self.connection.commit()

    # INSERT statement for inserting student data to database
    def add_student(self, id, fn, ln, e, g, a, ad, ctc, m, crs):
        query = (
            "INSERT INTO students (id, st_name, st_lastname, st_email, gender, age, address, contact, courseMode, course) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
        self.cursor.execute(query, (id, fn, ln, e, g, a, ad, ctc, m, crs))
        self.connection.commit()

    # INSERT statement for inserting lecturer data to database
    def add_lecturer(self, id, fn, ln, e, g, a):
        query = "INSERT INTO lecturers (id, lt_name, lt_lastName, lt_email, gender, age) VALUES (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (id, fn, ln, e, g, a))
        self.connection.commit()

    # DELETE statement to delete student row data
    def delete_student(self, id):
        query = "DELETE FROM students WHERE id = ?"
        self.cursor.execute(query, (id,))
        self.connection.commit()

    # DELETE statement to delete lecturer row data
    def delete_lecturer(self, id):
        query = "DELETE FROM lecturers WHERE id = ?"
        self.cursor.execute(query, (id,))
        self.connection.commit()

    # UPDATE statement to update student data
    def update_student(self, fn, ln, e, g, a, ad, ctc, m, crs, id):
        query = "UPDATE students SET st_name=?, st_lastname=?, st_email=?, gender=?, age=?, address=?, contact=?, courseMode=?, course=? WHERE id = ?"
        self.cursor.execute(query, (fn, ln, e, g, a, ad, ctc, m, crs, id,))

        self.connection.commit()

    # UPDATE statement to update lecturer data
    def update_lecturer(self, fn, ln, e, g, a, id):
        query = "UPDATE lecturers SET lt_name=?, lt_lastName=?, lt_email=?, gender=?, age=? WHERE id = ?"
        self.cursor.execute(query, (fn, ln, e, g, a, id))

        self.connection.commit()

    # Dynamic SELECT statement for fetching table data
    def fetch_data(self, table):
        query = (f"SELECT * FROM {table}")
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    # Sample data
    """
    def populate_students(self):
        # Sample data for students
        sample_students = [
            ("John", "Doe", "john@example.com", "Male", 25, "123 Main St", "1234567890", "Full-time",
             "Computer Science"),
            ("Jane", "Smith", "jane@example.com", "Female", 23, "456 Elm St", "0987654321", "Part-time", "Engineering"),
            ("Michael", "Johnson", "michael@example.com", "Male", 22, "789 Oak St", "9876543210", "Full-time",
             "Mathematics"),
            ("Emily", "Brown", "emily@example.com", "Female", 24, "101 Pine St", "4567890123", "Part-time", "Physics"),
            ("Daniel", "Martinez", "daniel@example.com", "Male", 21, "202 Cedar St", "1357924680", "Full-time",
             "Chemistry"),
            ("Sarah", "Jones", "sarah@example.com", "Female", 26, "303 Maple St", "2468013579", "Part-time", "Biology"),
            ("Christopher", "Garcia", "chris@example.com", "Male", 20, "404 Birch St", "3692581470", "Full-time",
             "Computer Engineering"),
            ("Jessica", "Hernandez", "jessica@example.com", "Female", 22, "505 Walnut St", "5820463719", "Part-time",
             "Electrical Engineering"),
            ("Matthew", "Lopez", "matthew@example.com", "Male", 23, "606 Pineapple St", "7930158246", "Full-time",
             "Civil Engineering"),
            ("Amanda", "Gonzalez", "amanda@example.com", "Female", 24, "707 Mango St", "2468013579", "Part-time",
             "Mechanical Engineering"),
            ("David", "Perez", "david@example.com", "Male", 25, "808 Banana St", "1357924680", "Full-time",
             "Aerospace Engineering"),
            ("Ashley", "Wilson", "ashley@example.com", "Female", 26, "909 Papaya St", "5820463719", "Part-time",
             "Industrial Engineering"),
            ("James", "Anderson", "james@example.com", "Male", 21, "111 Apple St", "3692581470", "Full-time",
             "Environmental Engineering"),
            ("Melissa", "Taylor", "melissa@example.com", "Female", 22, "222 Orange St", "1234567890", "Part-time",
             "Software Engineering"),
            ("Ryan", "Thomas", "ryan@example.com", "Male", 23, "333 Grape St", "0987654321", "Full-time",
             "Data Science"),
            ("Nicole", "Moore", "nicole@example.com", "Female", 24, "444 Cherry St", "1357924680", "Part-time",
             "Computer Animation"),
            ("Taylor", "Jackson", "taylor@example.com", "Male", 25, "555 Lemon St", "2468013579", "Full-time",
             "Graphic Design"),
            ("Andrew", "White", "andrew@example.com", "Male", 26, "666 Lime St", "5820463719", "Part-time",
             "Fashion Design"),
            ("Olivia", "Harris", "olivia@example.com", "Female", 27, "777 Avocado St", "3692581470", "Full-time",
             "Interior Design"),
            ("Jacob", "Martin", "jacob@example.com", "Male", 28, "888 Kiwi St", "1234567890", "Part-time",
             "Architecture"),
        ]

        for student in sample_students:
            self.cursor.execute('''INSERT INTO students (st_name, st_lastname, st_email, gender, age, address, contact, courseMode, course)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', student)

    # sample data for lecturers
    def populate_lecturers(self):
        sample_lecturers = [
            (331, "John", "Doe", "john@example.com", "Male", 45),
            (440, "Jane", "Smith", "jane@example.com", "Female", 40),
            (3, "Michael", "Johnson", "michael@example.com", "Male", 50),
            (4, "Emily", "Brown", "emily@example.com", "Female", 42),
            (5, "Daniel", "Martinez", "daniel@example.com", "Male", 48),
            (6, "Sarah", "Jones", "sarah@example.com", "Female", 47),
            (7, "Christopher", "Garcia", "chris@example.com", "Male", 43),
            (8, "Jessica", "Hernandez", "jessica@example.com", "Female", 41),
            (9, "Matthew", "Lopez", "matthew@example.com", "Male", 49),
            (10, "Amanda", "Gonzalez", "amanda@example.com", "Female", 46),
            (11, "David", "Perez", "david@example.com", "Male", 44),
            (12, "Ashley", "Wilson", "ashley@example.com", "Female", 39),
            (13, "James", "Anderson", "james@example.com", "Male", 38),
            (14, "Melissa", "Taylor", "melissa@example.com", "Female", 37),
            (15, "Ryan", "Thomas", "ryan@example.com", "Male", 36),
            (16, "Nicole", "Moore", "nicole@example.com", "Female", 35),
            (17, "Taylor", "Jackson", "taylor@example.com", "Male", 34),
            (18, "Andrew", "White", "andrew@example.com", "Male", 33),
            (19, "Olivia", "Harris", "olivia@example.com", "Female", 32),
            (20, "Jacob", "Martin", "jacob@example.com", "Male", 31),
        ]

        for student in sample_lecturers:
            self.cursor.execute("INSERT INTO lecturers (id, lt_name, lt_lastName, lt_email, gender, age) VALUES (?, ?, ?, ?, ?, ?)", student)
    """

    # Dynamic SELECT statement for returning search results
    def search(self, table, search_term):
        if table == "lecturers":
            # SQL wildcard and partial string matching for dynamic and flexible searches
            query = "SELECT * FROM lecturers WHERE id LIKE ? OR lt_name LIKE ? OR lt_lastname LIKE ? OR lt_email LIKE ? OR gender LIKE ? OR age LIKE ?"
            self.cursor.execute(query, (('%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%')))
            rows = self.cursor.fetchall()
        else:
            query = "SELECT * FROM students WHERE id LIKE ? OR st_name LIKE ? OR st_lastname LIKE ? OR st_email LIKE ? OR gender LIKE ? OR age LIKE ? OR address LIKE ? OR contact LIKE ? OR courseMode LIKE ? OR course LIKE ? "
            self.cursor.execute(query, (('%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%')))
            rows = self.cursor.fetchall()
        return rows

    # SELECT statement for id's
    def entry_exists(self, table, id):
        query = f"SELECT * FROM {table} WHERE id = ?"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchall()
        return result

    def __del__(self):
        self.connection.close()
