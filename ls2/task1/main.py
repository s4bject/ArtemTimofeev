from database import engine
from models import *

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы!")