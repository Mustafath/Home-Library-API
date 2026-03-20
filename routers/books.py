from fastapi import APIRouter, status
from schemas.books import SBookAdd, SBook, SBookPatch, SBookUpdate
from models.books import Book
from database import SessionDep
from repository.books import Repository

router = APIRouter(prefix="/books", tags=["Книги"])


@router.get("/{book_id}", status_code=status.HTTP_200_OK)
async def get_book(book_id: int, session: SessionDep) -> SBook:
    result = await Repository.get_book(book_id, session)
    return result


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_books(session: SessionDep) -> list[SBook]:
    result = await Repository.get_all_books(session)
    return result


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_book(book: SBookAdd, session: SessionDep) -> SBook:
    result = await Repository.add_book(book, session)
    return result


@router.put("/{book_id}", status_code=status.HTTP_200_OK)
async def put_book(book_id: int, book: SBookUpdate, session: SessionDep) -> SBook:
    result = await Repository.put_book(book_id, book, session)
    return result


@router.patch("/{book_id}", status_code=status.HTTP_200_OK)
async def patch_book(book_id: int, book:SBookPatch, session: SessionDep) -> SBook:
    result = await Repository.patch_book(book_id, book, session)
    return result


@router.delete("/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: int, session: SessionDep) -> SBook:
    result = await Repository.delete_book(book_id, session)
    return result