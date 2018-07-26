import requests
from bs4 import BeautifulSoup


class Scraper:
    __request_url = ""
    __response = ""
    __soup = None

    def __init__(self, request_url):
        self.__request_url = request_url

    def set_request_url(self, request_url):
        if isinstance(request_url, str):
            self.__request_url = request_url

    def get_response(self):
        return self.__response

    def query(self):
        if self.__request_url != "":
            self.__response = requests.get(self.__request_url)

    def print_response(self):
        print(self.__response.text)

    def parse(self):
        if self.__response != "":
            self.__soup = BeautifulSoup(self.__response.text, "html.parser")

    def get_tags(self , tag):
        if self.__soup is not None:
            return self.__soup.find_all(tag)

    def print_tags(self , tag):
        if self.__soup is not None:
            print(self.__soup.find_all(tag))
            # @staticmethod
    # def print_soup(soup, tag):
    #     print(soup.find_all(tag))
