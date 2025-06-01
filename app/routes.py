from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .models import Device
from .db import get_db

router = APIRouter()

@router.get("/apps")
def get_applications(db: Session = Depends(get_db)):
    result = db.query(Device.application).distinct().all()
    return [r.application for r in result if r.application]
