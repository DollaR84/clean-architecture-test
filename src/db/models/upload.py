import uuid

from application.types import StatusType

import sqlalchemy as sa
import sqlalchemy.orm as so

from sqlalchemy.dialects.postgresql import UUID as PgUUID
from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from .base import BaseDBModel

from ..base import Base


class FileUpload(BaseDBModel, Base):

    filename: so.Mapped[str] = so.mapped_column(nullable=True)


class Upload(BaseDBModel, Base):

    uuid_id: so.Mapped[uuid.UUID] = so.mapped_column(
        PgUUID(as_uuid=True),
        unique=True,
        nullable=False,
        default=uuid.uuid4,
    )

    urls: so.Mapped[str] = so.mapped_column(nullable=True)
    file_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("file_uploads.id"), nullable=True)
    file: so.Mapped["FileUpload"] = so.relationship(foreign_keys=file_id)

    status: so.Mapped[StatusType] = so.mapped_column(
        PgEnum(StatusType, name="status_type", create_type=False),
        nullable=False,
        default=StatusType.NOT_STARTED,
    )
