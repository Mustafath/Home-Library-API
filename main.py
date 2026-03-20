import uvicorn
from fastapi import FastAPI
from routers.books import router as books_router
from contextlib import asynccontextmanager
from database import engine
from models.books import Model


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- КОД ПРИ СТАРТЕ ---
    print("Сервер запущен")

    # Мы обращаемся к движку и просим создать все таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
    
    print("База данных готова к работе")
    
    yield  # Разделяет старт и выключение
    
    # --- КОД ПРИ ВЫКЛЮЧЕНИИ ---
    print("Выключение сервера")


app = FastAPI(lifespan=lifespan, title="Домашняя библиотека", version='1.0.0')

app.include_router(books_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, workers=4)