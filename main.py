# Wordle
from game import Game
from word import Word
from player import Player

def main():
    width, height = 5,6
    url = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"
    game = Game(width, height)
    word = Word(url)
    player = Player(game, word)
    player.begin_game()

if __name__ == '__main__':
    main()
