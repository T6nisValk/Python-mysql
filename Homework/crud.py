from models import eng, TodoLists, TodoItems
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=eng)
session = Session()


def create_todo_list(title):
    session.add(TodoLists(title=title))
    session.commit()


def create_task(list_id, name):
    session.add(TodoItems(name=name, list_id=list_id))
    session.commit()


def select_tasks():
    return session.query(TodoItems).all()


def select_task(id):
    return session.query(TodoItems).where(TodoItems.item_id == id).first()


def select_lists():
    return session.query(TodoLists).all()


def select_list(id):
    return session.query(TodoLists).where(TodoLists.list_id == id).first()


def make_complete(id):
    task = select_task(id)
    task.state = True
    session.commit()


def make_not_complete(id):
    task = select_task(id)
    task.state = False
    session.commit()


def delete_task(id):
    task = select_task(id)
    session.delete(task)
    session.commit()


def delete_list(id):
    list = select_list(id)
    # If I delete the list, then I have to delete all tasks that are for that list?
    # Otherwise tasks are linked to a non existent list.
    tasks = select_tasks()
    for task in tasks:
        if task.list_id == id:
            session.delete(task)
    session.delete(list)
    session.commit()
