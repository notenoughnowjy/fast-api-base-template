from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.deps import get_db
from app.crud.item import item as crud_item
from app.schemas.item import ItemCreate, ItemResponse

router = APIRouter()


@router.post("/", response_model=ItemResponse)
def create_item(item_in: ItemCreate, db: Session = Depends(get_db)):
    """새 아이템 생성"""
    return crud_item.create(db=db, obj_in=item_in)


@router.get("/", response_model=list[ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """모든 아이템 조회"""
    return crud_item.get_multi(db=db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """특정 아이템 조회"""
    db_item = crud_item.get(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.delete("/{item_id}", response_model=ItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """아이템 삭제"""
    db_item = crud_item.delete(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

