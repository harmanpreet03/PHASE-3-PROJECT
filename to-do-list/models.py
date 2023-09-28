from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TodoList(Base):
    __tablename__ = 'todolists'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    tasks = relationship('Task', back_populates='todolist')

    def __str__(self):
        return self.name


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)

    todolist_id = Column(Integer, ForeignKey('todolists.id'))
    todolist = relationship('TodoList', back_populates='tasks')

    def __str__(self):
        return f'Task: {self.description} (Completed: {self.completed})'


engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
