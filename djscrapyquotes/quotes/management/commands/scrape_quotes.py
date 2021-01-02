from django.core.management import BaseCommand


class Command(BaseCommand):

    help = "Scrape the quotes"

    def handle(self, *args, **kwargs):
        print("hello runing command")
