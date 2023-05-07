from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class DonationCreate(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]


class DonationDB(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationFullDB(DonationDB):
    user_id: Optional[int]
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]
