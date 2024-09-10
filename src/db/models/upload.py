import uuid

from application.types import StatusType

import sqlalchemy as sa
import sqlalchemy.orm as so

from .base import BaseDBModel

from ..base import Base


class FileUpload(BaseDBModel, Base):

    filename: so.Mapped[str] = so.mapped_column(nullable=True)


class Upload(BaseDBModel, Base):

    uuid_id: so.Mapped[str] = so.mapped_column(
        sa.String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4()),
    )

    urls: so.Mapped[str] = so.mapped_column(nullable=False)
    file_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("file_uploads.id"), nullable=True)
    file: so.Mapped["FileUpload"] = so.relationship(foreign_keys=file_id)

    status: so.Mapped[StatusType] = so.mapped_column(
        sa.Enum(StatusType),
        nullable=False,
        default=StatusType.NOT_STARTED,
    )
