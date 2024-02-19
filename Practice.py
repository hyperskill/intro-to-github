import sys
import os
import re
import requests
from bs4 import BeautifulSoup
from collections import deque


class Browser:
    def __init__(self):
        self.history = deque()
        self.directory = ''
        self.current_file = ''
        self.files = []
        self.my_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']

    def get_directory(self) -> None:
        try:
            self.directory = sys.argv[1]
            os.mkdir(self.directory)
        except IndexError:
            sys.exit()
        except FileExistsError:
            pass

    def get_files(self) -> None:
        self.files = os.listdir(self.directory)

    def get_url(self) -> str:
        while True:
            url = input()
            if url == 'exit':
                sys.exit()
            elif url == 'back':
                return self.history.pop() if self.history else ''
            return url

    def print_page(self, url: str) -> str | None:
        if not url:
            return

        if url in self.files:  # if the file already exists...
            self.print_file(url)
            self.add_to_history(url)
            return

        match = re.search(r'([^.]+)\..+$', url)
        if not match:
            return 'Invalid URL'  # No dot in the URL

        file = match.group(1)  # Get the file name

        if not url.startswith(r'https://'):
            url = r'https://' + url

        try:
            response = requests.get(url)  # Get the response
        except Exception:
            return 'Invalid URL'
        if response.status_code != requests.codes.ok:
            return 'Invalid URL'

        my_text = self.get_content(response.content)
        with open(f'{self.directory}/{file}', mode='w', encoding="utf-8") as f:
            f.write(my_text)
        self.files.append(file)
        print(my_text)

        self.add_to_history(file)

    def print_file(self, file):
        with open(f'{self.directory}/{file}', mode='r', encoding="utf-8") as f:
            print(f.read())

    def add_to_history(self, file):
        if self.current_file:
            self.history.append(self.current_file)  # old current url to history
        self.current_file = file  # set new current url

    def get_content(self, content) -> str:
        soup = BeautifulSoup(content, 'html.parser')
        all_text = ''
        for element in soup.find_all(self.my_tags):
            if element.name == 'a':
                all_text += ('\033[34m' + element.text + '\033[39m')
            else:
                all_text += element.text
        return all_text

    def main_cycle(self) -> None:
        self.get_directory()
        self.get_files()
        while True:
            url = self.get_url()
            result = self.print_page(url)
            if result:
                print(result)


if __name__ == '__main__':
    my_browser = Browser()
    my_browser.main_cycle()
