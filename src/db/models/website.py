import sqlalchemy.orm as so

from .base import BaseDBModel

from ..base import Base


class WebsiteInfo(BaseDBModel, Base):

    website: so.Mapped[str] = so.mapped_column(nullable=False, unique=True)
    emails: so.Mapped[str] = so.mapped_column(nullable=True)
    phones: so.Mapped[str] = so.mapped_column(nullable=True)
