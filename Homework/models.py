from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

eng = create_engine("sqlite:///todo_app.db")
Base = declarative_base()


class TodoLists(Base):
    __tablename__ = "todo_lists"

    list_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)

    items = relationship("TodoItems", backref="todo_lists", cascade="all, delete-orphan")


class TodoItems(Base):
    __tablename__ = "todo_items"

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    list_id = Column(Integer, ForeignKey("todo_lists.list_id", ondelete="CASCADE"))
    state = Column(Boolean, default=False)

    def __repr__(self):
        return f"{self.item_id}: {self.name}"


if __name__ == "__main__":
    Base.metadata.create_all(eng)
