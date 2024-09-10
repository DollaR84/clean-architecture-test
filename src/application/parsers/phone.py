import logging
import re

from .base import BaseParser


class PhoneParser(BaseParser):

    def get(self) -> list[str]:
        try:
            phone_pattern = (r"(\+\d{1,2}\(\d{3}\)\ \d{3}\-\d{2}\-\d{2})|(\+\d{1,2}"
                             r"\(\d{3}\)\d{3}\-\d{2}\-\d{2})|(\+\d{12})|(\d{11})|"
                             r"(\+\d{1,2}\(\d{3}\)\d{3}\d{2}\d{2})|(\d{1,2}\(\d{3}\)"
                             r"\d{3}\d{2}\d{2})|(\+\d{1,2}\ \(\d{3}\)\ \d{3}[- ]\d{2}"
                             r"[- \d]\d{2})|(\d{10})|(\(\d{3}\)\ \d{3}\ \d{4})|(\d)"
                             r"(\(\d{3}\)\ \d{3}\ \d{2}\ \d{2})|(\d{3}\ \d{3}\ \d{4})"
                             )

            phone = re.findall(phone_pattern, self.html)
            nodup_phone = self.remove_duplicates(phone)

            return [i for tup in nodup_phone for i in tup if i != '']
        except Exception as e:
            logging.error(f"Phone search error: {e}")
