import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
SELECT s.name, s.major, c.course_name, c.instructor
FROM student_courses sc
JOIN students s ON sc.student_id = s.id
JOIN courses c ON sc.course_id = c.course_id;
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
