from django.core.management import BaseCommand

import os
from pathlib import Path

class Command(BaseCommand):

    help = "Scrape the quotes from specific author"

    def add_arguments(self, parser):
        parser.add_argument('author_name',
                            type=str, help="Name of the author, parts of name separated by '-'")

    def handle(self, *args, **kwargs):
        django_path = Path(__file__).resolve().parent.parent.parent.parent
        os.chdir(str(django_path)+"/scraper/")
        os.system("scrapy crawl some-quotes -a author='{}' -L WARN".format(kwargs['author_name']))
        
