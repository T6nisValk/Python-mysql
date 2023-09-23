create_database_query = """CREATE DATABASE IF NOT EXISTS todo_app"""

create_tables_query = """CREATE TABLE IF NOT EXISTS todo_lists(
    list_id INT PRIMARY KEY AUTO_INCREMENT, 
    title VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS todo_items(
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    state BOOLEAN NOT NULL,
    list_id INT NOT NULL,
    FOREIGN KEY (list_id) REFERENCES todo_lists(list_id)
);
"""


def add_todo_list_query(title):
    return f"INSERT INTO todo_lists (title) VALUES ('{title}');"


def create_item_to_list(list_id, name):
    return f"INSERT INTO todo_items (name, state, list_id) VALUES ('{name}', False, '{list_id}')"
