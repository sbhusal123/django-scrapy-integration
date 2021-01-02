# Integrating django with scrapy

## 1. Packages Used:

-   [scrapy](https://docs.scrapy.org/en/latest/) for scraping quotes from [this](https://quotes.toscrape.com/) site.
-   [coloredlogs](https://pypi.org/project/coloredlogs/) for colorful logging messages.
-   **Install packages:** `pip install -r requirements.txt`

## 2. Spiders

[Spiders](https://github.com/sbhusal123/django-scrapy-integration/tree/main/djscrapyquotes/scraper/scraper/spiders)

[Scrapy project](https://github.com/sbhusal123/django-scrapy-integration/tree/main/djscrapyquotes/scraper)

> Before executing commands below make sure. You're inside **scraper** folder. `cd scraper`

**i. QuotesSpider:**

-   Extracts and populates all the quotes with the author name.
-   **Execute Spider:** `scrapy crawl quotes -L WARN`

**ii. SpecificAuthorQuotesSpider:**

-   Extracts and populates quotes from specific author.
-   **Execute Spider:** `scrapy crawl some-quotes -a author="Albert Einstein" -L WARN`

[Integration and django setup inside scrapy project](https://github.com/sbhusal123/django-scrapy-integration/blob/main/djscrapyquotes/scraper/scraper/settings.py#L95)

```python
# ------------------------ Django Integration -----------------------------

# Django project root level path
django_path = Path(__file__).resolve().parent.parent.parent

# append the django project path to the system path. Allows us to import django stuffs
sys.path.append(str(django_path)+"/")

# Setup django. Allows us to perform database related operations importing models from dj project.
os.environ['DJANGO_SETTINGS_MODULE'] = 'djscrapyquotes.settings'
django.setup()

# This import should be here
# from quotes.models import Quotes
# ----------------------------------------------------------------------
```
