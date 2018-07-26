from mod.scraping.Scraper import Scraper
from mod.sqlite.SqliteService import SqliteService

url = "https://github.com/zoo-chee/scraping"
# url = "https://raw.githubusercontent.com/zoo-chee/scraping/master/test/test.md"
scraper = Scraper(url)
scraper.query()
# scraper.print_response()
scraper.parse()
# scraper.print_tags('a')

for link in scraper.get_tags('a'):
    print(link.get('href'))

service = SqliteService()
service.createDb()
service.commit()