import sqlite3


with sqlite3.connect("test.db") as conn:
    all_food = conn.execute("SELECT * FROM food")
    for food in all_food:
        print(food)
    
    conn.execute("INSERT INTO food (name, price) VALUES ('salad', 7.77)")
    conn.commit()

    all_food_again = conn.execute("SELECT * FROM food")
    for food in all_food_again:
        print(food)
