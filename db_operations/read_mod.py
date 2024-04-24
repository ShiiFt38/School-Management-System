from tkinter import messagebox


class Read:
    def __init__(self, db):
        self.db = db

    def populate_treeview(self, item, treeview, table):
        item.set("")

        treeview.delete(*treeview.get_children())
        if self.db.fetch_data(table):
            for row in self.db.fetch_data(table):
                treeview.insert("", "end", values=row)
        else:
            print("Could not fetch data")

    def search_entry(self, item, treeview, table):
        search_item = item.get()

        # Removes treeview data to show searched results
        for record in treeview.get_children():
            treeview.delete(record)

        if self.db.search(table, search_item):
            for row in self.db.search(table, search_item):
                treeview.insert("", "end", values=row)
        else:
            messagebox.showerror("Error", f"'{search_item}' not found.")