import random
import requests

class Word:
    def __init__(self, url):
        self.url = url
        self.lines = self.obtain_lines()

    def obtain_lines(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            lines = response.text.splitlines()
        else:
            print("Failed to retrieve the file.")
            lines = []
        return lines

    def new_word(self):
        list_size = len(self.lines)
        word_index = random.randint(0,list_size - 1)
        word = self.lines[word_index].upper()
        return word



