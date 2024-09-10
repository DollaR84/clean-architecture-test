import logging

from bs4 import BeautifulSoup

from application.dto import ContactData

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .base import BaseParser

from .types import ParserType


class Parser:

    def __init__(
            self,
            url: str,
            parsers: BaseParser = BaseParser,
    ):
        self.url: str = url
        self.parsers: BaseParser = BaseParser

        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("disable-infobars")

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(self.url)

    def get_data(self) -> ContactData:
        contact = ContactData(website=self.url)
        try:
            info = BeautifulSoup(self.driver.page_source, 'lxml')
            html = info.get_text()

            emails = self.parsers.get_parser(ParserType.EMail)(html).get()
            phones = self.parsers.get_parser(ParserType.Phone)(html).get()

            contact.emails.extend(emails)
            contact.phones.extend(phones)

            contact_parser = self.parsers.get_parser(ParserType.Contact)(html, info=info, driver=self.driver)
            contact = contact_parser.get(contact)

        except Exception as e:
            logging.error(e, exc_info=True)

        finally:
            self.driver.quit()

        return contact
