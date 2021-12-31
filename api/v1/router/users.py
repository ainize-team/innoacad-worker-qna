from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from core.models.user_model import UserModel
from core.schemas.user_schema import UserBase

router = APIRouter()


@router.get("/{username}", response_model=UserBase)
def getUser(
    username: str, db: Session = Depends(get_db),
):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user
