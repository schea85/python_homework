import sqlite3
import pandas as pd

# TASK 5:
with sqlite3.connect("../db/lesson.db") as conn:
    # join tables
    sql_statement = """ SELECT line_items.line_item_id, line_items.quantity, line_items.product_id, products.product_name, products.price 
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    """
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head())
     
     # add total column
    df["total"] = df["quantity"] * df["price"]
    print(df.head(5))
    
    # groupby/agg 
    df= df.groupby("product_id").agg({"line_item_id": "count", "total": "sum", "product_name": "first"})
    print(df.head())
    
    # sort
    df = df.sort_values(by="product_name", ascending=True)
    
    # csv
    df.to_csv("order_summary.csv")
    
    