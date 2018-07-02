from mod.scraping.Scraper import Scraper

url = "https://github.com/zoo-chee/scraping"
scraper = Scraper(url)
scraper.query()
scraper.print_response()