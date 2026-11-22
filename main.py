import sqlite3


conn = sqlite3.connect("university.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        major TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT,
        instructor TEXT
    )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_courses (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
""")
conn.commit()


while True:
    print("\n1. Додати студента")
    print("2. Додати курс")
    print("3. Показати студентів")
    print("4. Показати курси")
    print("5. Змінити студента")
    print("6. Змінити курс")
    print("7. Записати студента на курс")
    print("8. Студенти на курсі")
    print("0. Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        break
    elif choice == "2":
        break
    elif choice == "3":
        break
    elif choice == "4":
        break
    elif choice == "5":
        break
    elif choice == "6":
        break
    elif choice == "7":
        break
    else:
        print("Некоректний вибір")
