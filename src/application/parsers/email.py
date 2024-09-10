import logging
import re

from .base import BaseParser


class EMailParser(BaseParser):

    def get(self) -> list[str]:
        try:
            email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", self.html)
            nodup_email = self.remove_duplicates(email)

            return [i for i in nodup_email]
        except Exception as e:
            logging.error(f"Email search error: {e}")
