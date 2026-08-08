import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ---------- DATABASE CONNECTION & SETUP ----------
try:
    # First connect without database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""   
    )
    cursor = db.cursor()

    # Create database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
    cursor.execute("USE student_db")

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll INT PRIMARY KEY,
            name VARCHAR(50),
            course VARCHAR(50),
            marks INT
        )
    """)

except mysql.connector.Error as e:
    print("Database Error:", e)
    exit()

# ---------- FUNCTIONS ----------
def add_student():
    r = roll_entry.get()
    n = name_entry.get()
    c = course_entry.get()
    m = marks_entry.get()

    if r == "" or n == "" or c == "" or m == "":
        messagebox.showwarning("Input Error", "All fields are required")
        return

    try:
        cursor.execute(
            "INSERT INTO students VALUES (%s,%s,%s,%s)",
            (r, n, c, m)
        )
        db.commit()
        messagebox.showinfo("Success", "Student Added Successfully")
        clear_fields()
    except:
        messagebox.showerror("Error", "Roll number already exists")


def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    output.delete(1.0, tk.END)
    output.insert(tk.END, "Roll  Name  Course  Marks\n")
    output.insert(tk.END, "-" * 35 + "\n")

    for row in records:
        output.insert(
            tk.END,
            f"{row[0]}    {row[1]}    {row[2]}    {row[3]}\n"
        )


def update_student():
    r = roll_entry.get()
    n = name_entry.get()
    c = course_entry.get()
    m = marks_entry.get()

    cursor.execute(
        "UPDATE students SET name=%s, course=%s, marks=%s WHERE roll=%s",
        (n, c, m, r)
    )
    db.commit()
    messagebox.showinfo("Updated", "Student Updated Successfully")
    clear_fields()


def delete_student():
    r = roll_entry.get()
    cursor.execute("DELETE FROM students WHERE roll=%s", (r,))
    db.commit()
    messagebox.showinfo("Deleted", "Student Deleted Successfully")
    clear_fields()


def clear_fields():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)


# ---------- GUI ----------
root = tk.Tk()
root.title("Student Management System")
root.geometry("450x480")

tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(root, text="Roll No").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()

tk.Label(root, text="Marks").pack()
marks_entry = tk.Entry(root)
marks_entry.pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)
tk.Button(root, text="Update Student", command=update_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

output = tk.Text(root, height=9, width=50)
output.pack(pady=10)

root.mainloop()
