from sqlalchemy.orm import DeclarativeBase

from app.db.session import engine


class Base(DeclarativeBase):
    pass


def init_db() -> None:
    """Create database tables from SQLAlchemy metadata."""
    Base.metadata.create_all(bind=engine)
