import sqlite3

# Connect to the BD
conn = sqlite3.connect('university.db')
c = conn.cursor()

# examples

# All students
query_1 = """
SELECT * from students;
"""

# All teachers
query_2 = """
SELECT * from teachers;
"""

# Execution of queries and display of results
print("query 1:")
c.execute(query_1)
result_1 = c.fetchall()
for row in result_1:
    print(row)

print("query 2:")
c.execute(query_2)
result_2 = c.fetchall()
for row in result_2:
    print(row)

# Close the connection to the database
conn.close()