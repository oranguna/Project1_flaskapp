import psycopg2


db_name = "your_database_name"
db_user = "your_username"
db_password = "your_password"
db_host = "localhost"
db_port = "5432"

try:

    conn = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)

    
    cur = conn.cursor()

 
    cur.execute("DROP TABLE IF EXISTS employees;")
    cur.execute("""
        CREATE TABLE employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INTEGER,
            department VARCHAR(255)
        );
    """)


    cur.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ("Alice", 30, "Sales"))
    cur.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", ("Bob", 25, "Marketing"))

    
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    print("Employees:")
    for row in rows:
        print(row)

    
    cur.execute("UPDATE employees SET age = %s WHERE name = %s", (31, "Alice"))


    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    print("\nUpdated Employees:")
    for row in rows:
        print(row)

    
    cur.execute("DELETE FROM employees WHERE name = %s", ("Bob",))


    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    print("\nEmployees after deletion:")
    for row in rows:
        print(row)

  
    conn.commit()

except psycopg2.Error as e:
    print(f"Database error: {e}")

finally:
   
    if cur:
        cur.close()
    if conn:
        conn.close()
    
                      

