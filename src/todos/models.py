import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base

class TaskModel(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(default='')
    description: Mapped[str] = mapped_column(default='')
    complit: Mapped[bool] = mapped_column(default=False)
