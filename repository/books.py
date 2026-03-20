from sqlalchemy import select, insert, update, delete
from models.books import Book
from schemas.books import SBookAdd, SBookUpdate, SBookPatch
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

class Repository:
    async def get_book(book_id: int, session: AsyncSession) -> Book:
        result = await session.execute(select(Book).where(Book.id == book_id))
        return result.scalar_one_or_none()

    async def get_all_books(session: AsyncSession) -> list[Book]:
        result = await session.execute(select(Book))
        return result.scalars().all()
    
    async def add_book(book: SBookAdd, session: AsyncSession) -> Book:
        new_book = Book(**book.model_dump())
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book
    
    async def put_book(book_id: int, book: SBookUpdate, session: AsyncSession) -> Book:
        result = await session.execute(select(Book).where(Book.id == book_id))
        new_book = result.scalar_one_or_none()
        if not new_book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            
        for attr, value in book.model_dump().items():
            setattr(new_book, attr, value)

        await session.commit()
        return new_book
    
    async def patch_book(book_id: int, book: SBookPatch, session: AsyncSession) -> Book:
        result = await session.execute(select(Book).where(Book.id == book_id))
        new_book = result.scalar_one_or_none()
        if not new_book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        for attr, value in book.model_dump(exclude_unset=True).items():
            setattr(new_book, attr, value)

        await session.commit()
        return new_book
    
    async def delete_book(book_id: int, session: AsyncSession) -> Book:
        book = await session.get(Book, book_id)
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        await session.delete(book)
        await session.commit()
        return book
    