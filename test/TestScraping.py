import unittest
from mod.scraping.Scraper import Scraper


class TestScraping(unittest.TestCase):
    def test_query(self):
        url = "https://raw.githubusercontent.com/zoo-chee/scraping/master/test/test.md"
        scraper = Scraper(url)
        scraper.query()
        response = scraper.get_response()
        self.assertEqual("It's test file." , response.text)

if __name__ == '__main__':
    unittest.main()