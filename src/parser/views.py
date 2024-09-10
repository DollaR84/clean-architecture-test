from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .models import FileUpload, WebsiteInfo

import logging
from threading import Thread
from queue import Queue

from application.parsers import Parser


def read_file(file_content):
    urls = []
    for line in file_content.split('\n'):
        url = line.strip()
        if not url.startswith('http'):
            url = 'https://' + url
        urls.append(url)
    return urls


def crawl(q, result):
    while not q.empty():
        url = q.get()
        logging.info(f'Searched home URL: {url[1]}')

        try:
            parser = Parser(url[1])
            contact = parser.get_data()

            result['Website'].append(contact.website)
            result['Email'].append(contact.emails)
            result['Phone'].append(contact.phones)

        except Exception as e:
            logging.error(f"Request error in threads: {e}")
            result['Website'].append(url[1])
            result['Email'].append([])
            result['Phone'].append([])

        finally:
            q.task_done()
            logging.debug(f"Queue task no {url[0]} completed.")
    return True


def parse_and_save_data(request):
    try:
        latest_file = FileUpload.objects.latest('id')
        file_path = default_storage.path(latest_file.file.name)

        with open(file_path, 'r') as file:
            file_content = file.read()
    except FileUpload.DoesNotExist:
        return HttpResponse('No files found for parsing.')

    urls = read_file(file_content)

    q = Queue(maxsize=0)
    num_threads = min(50, len(urls))

    results = {'Website': [], 'Email': [], 'Phone': []}

    for i in range(len(urls)):
        q.put((i, urls[i]))

    for i in range(num_threads):
        logging.debug(f"Starting thread: {i}")
        worker = Thread(target=crawl, args=(q, results))
        worker.daemon = True
        worker.start()

    q.join()

    for website, email, phone in zip(results['Website'], results['Email'], results['Phone']):
        WebsiteInfo.objects.create(website=website, emails=','.join(email), phones=','.join(phone))

    return HttpResponse('Data parsed and saved!')


@receiver(post_save, sender=FileUpload)
def trigger_parser(sender, instance, **kwargs):
    parse_and_save_data(instance.file.path)
