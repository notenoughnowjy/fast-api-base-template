from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.item import ItemCreate


class CRUDItem:
    def get(self, db: Session, item_id: int) -> Item | None:
        return db.query(Item).filter(Item.id == item_id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> list[Item]:
        return db.query(Item).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: ItemCreate) -> Item:
        db_item = Item(name=obj_in.name, description=obj_in.description)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def delete(self, db: Session, item_id: int) -> Item | None:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item:
            db.delete(db_item)
            db.commit()
        return db_item


item = CRUDItem()

