import requests
from bs4 import BeautifulSoup


class Scraper:
    __request_url = ""
    __response = ""

    def __init__(self, request_url):
        self.__request_url = request_url

    def set_request_url(self, request_url):
        if isinstance(url, str):
            self.__request_url = request_url

    def query(self):
        if self.__request_url != "":
            self.__response = requests.get(self.__request_url)

    def parse(self):
        if self.__response != "":
            soup = BeautifulSoup(self.__response, "html.parser")

    def print_response(self):
        print(self.__response.text)

    @staticmethod
    def print_soup(soup, tag):
        print(soup.find_all(tag))