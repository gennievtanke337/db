import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    major TEXT
)
""")

cursor.execute("""
               
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    instructor TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS student_courses (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")

conn.commit()

while True:
    print("\nСистема управління університетом")
    print("1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Переглянути всіх студентів")
    print("4. Переглянути всі курси")
    print("5. Зареєструвати студента на курс")
    print("6. Переглянути студентів на курсі")
    print("7. Вийти")

    choice = input("Виберіть опцію (1-7): ")
    
    if choice == "1":
        name = input("Ім'я студента: ")
        age = int(input("Вік студента: "))
        major = input("Спеціальність: ")
        cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
        conn.commit()
        print("Студента успішно додано!")
        
    elif choice == "2":
        course_name = input("Назва курсу: ")
        instructor = input("Ім'я викладача: ")
        cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (?, ?)", (course_name, instructor))
        conn.commit()
        print("Курс успішно додано!")
        
    elif choice == "3":
        cursor.execute("SELECT id, name, age, major FROM students")
        students = cursor.fetchall()
        print("\nСписок студентів:")
        for student in students:
            print(f"ID: {student[0]}, Ім'я: {student[1]}, Вік: {student[2]}, Спеціальність: {student[3]}")
            
    elif choice == "4":
        cursor.execute("SELECT course_id, course_name, instructor FROM courses")
        courses = cursor.fetchall()
        print("\nСписок курсів:")
        for course in courses:
            print(f"ID: {course[0]}, Назва: {course[1]}, Викладач: {course[2]}")
            
    elif choice == "5":
        student_id = int(input("ID студента: "))
        course_id = int(input("ID курсу: "))
        cursor.execute("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        conn.commit()
        print("Студента успішно зареєстровано на курс!")
        
    elif choice == "6":
        course_id = int(input("ID курсу: "))
        cursor.execute("""
        SELECT s.id, s.name, s.age, s.major 
        FROM students s
        JOIN student_courses sc ON s.id = sc.student_id
        WHERE sc.course_id = ?
        """, (course_id,))
        students = cursor.fetchall()
        print(f"\nСтуденти на курсі {course_id}:")
        for student in students:
            print(f"ID: {student[0]}, Ім'я: {student[1]}, Вік: {student[2]}, Спеціальність: {student[3]}")
            
    elif choice == "7":
        print("До побачення!")
        break
        
    else:
        print("Невірний вибір. Будь ласка, введіть число від 1 до 7.")

conn.close()