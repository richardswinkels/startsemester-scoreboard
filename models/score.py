from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from models.db import db
from datetime import datetime

class Score(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player_name: Mapped[str] = mapped_column(String(300))
    score: Mapped[int]
    bullets_used: Mapped[int]
    timestamp: Mapped[datetime] = mapped_column(default=func.now())

    def as_dict(self):
        return { 
            'player_name': self.player_name,
            'score': self.score,
            'bullets_used': self.bullets_used,
            'timestamp': self.timestamp
        }
