from models import Session

def init_db():
    from models import TodoList, Task

def get_session():
    return Session()
