import logging
import re

from application.dto import ContactData

from bs4 import BeautifulSoup

from .base import BaseParser
from .email import EMailParser
from .phone import PhoneParser


class ContactParser(BaseParser):

    def __init__(
            self,
            html: str,
            **kwargs
    ):
        super().__init__(html)

        self.info = kwargs.get("info")
        self.driver = kwargs.get("driver")

        if not all([self.info, self.driver]):
            raise ValueError(
                "Error initialization ContactParser. Additional arguments required: info, driver"
            )

    def get(self, contact: ContactData) -> ContactData:
        contact_element = self.info.find('a', string=re.compile('contact', re.IGNORECASE))
        if contact_element:
            contact = contact_element.get('href')
            if 'http' in contact:
                contact_url = contact
            else:
                contact_url = "/".join([self.driver.current_url[0:-1], contact])

            self.driver.get(contact_url)
            contact_info = BeautifulSoup(self.driver.page_source, 'lxml').get_text()
            logging.info(f'Searched contact URL: {self.driver.current_url}')

            contact.emails.extend(EMailParser(contact_info).get())
            contact.phones.extend(PhoneParser(contact_info).get())

            contact.emails = self.remove_duplicates(contact.emails)
            contact.phones = self.remove_duplicates(contact.phones)

        return contact
