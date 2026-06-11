import sqlite3

#########
# TASK 1:
#########
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query = """
    SELECT orders.order_id, SUM(products.price*line_items.quantity)
    FROM orders 
    JOIN line_items ON orders.order_id = line_items.order_id 
    JOIN products ON line_items.product_id = products.product_id 
    GROUP BY orders.order_id
    ORDER BY orders.order_id 
    LIMIT 5
"""

cursor.execute(query)
print("\nTask 1 answers: ", cursor.fetchall())

conn.close()

#########
# TASK 2:
#########
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query2 = """
    SELECT customers.customer_name, AVG(order_totals.total_price) AS average_total_price
    FROM customers
    LEFT JOIN (
        SELECT orders.order_id, orders.customer_id AS customer_id_b, SUM(products.price*line_items.quantity) AS total_price
        FROM orders 
        JOIN line_items ON orders.order_id = line_items.order_id 
        JOIN products ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
    ) AS order_totals
    ON customers.customer_id = order_totals.customer_id_b
    GROUP BY customers.customer_id
"""

cursor.execute(query2)
print("\nTask 2 answers: ", cursor.fetchall())

conn.close()

#########
# TASK 3:
######### 
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

try:
    query3 = """
        SELECT customers.customer_id
        FROM customers
        WHERE customers.customer_name = 'Perez and Sons'
    """
    cursor.execute(query3)
    customer_id = cursor.fetchone()[0]

    query4 = """
        SELECT employees.employee_id
        FROM employees
        WHERE employees.first_name = 'Miranda' AND employees.last_name = 'Harris'
    """
    cursor.execute(query4)
    employee_id = cursor.fetchone()[0]

    query5 = """
        SELECT products.product_id
        FROM products
        ORDER BY products.price
        LIMIT 5
    """
    cursor.execute(query5)
    product_ids = [row[0] for row in cursor.fetchall()]

    new_order = """
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id
    """
    cursor.execute(new_order, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    new_line_item = """
        INSERT INTO line_items (order_id, product_id, quantity)
        VALUES (?, ?, ?)
    """
    
    for product_id in product_ids:
        cursor.execute(new_line_item, (order_id, product_id, 10))
    conn.commit()
    
    verify_query = """
    SELECT line_items.line_item_id, line_items.quantity, products.product_name
    from line_items
    JOIN products
        ON line_items.product_id = products.product_id
    WHERE line_items.order_id = ?
"""
    cursor.execute(verify_query, (order_id,))
    results = cursor.fetchall()
    
    print("\nTask 3 answers: ", results)
    
    
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")

conn.close()

#########
# TASK 4:
#########
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

task_4_query = """
    SELECT  employees.employee_id, employees.first_name, employees.last_name, COUNT(orders.order_id) AS total_quantity
    FROM employees
    JOIN orders ON employees.employee_id = orders.employee_id
    GROUP BY employees.employee_id
    HAVING total_quantity > 5
"""

cursor.execute(task_4_query)
print("\nTask 4 answers: ", cursor.fetchall())

conn.close()



