# from game.word import Word
# from game.buffer import Buffer
# from game.inputService import InputService
# from game.outputService import OutputService
# from game.score import Score
# from game.actor import Actor
# from game import constants
# import random
# from game.point import Point
# from time import sleep

from word import Word
# from buffer import Buffer
from inputService import InputService
from outputService import OutputService
# from score import Score
# from actor import Actor
import constants
import random
from point import Point
# from time import sleep

class Director:
    def __init__(self):
        self._words = []
        # self._buffer = Buffer()
        # self._inputService = inputService
        # self._outputService = outputService
        # self._score = Score()

        for i in range(5):
            location = Point(random.randrange(0,40),random.randrange(1,19))
            velocity = Point(random.randrange(1,5),0)
            text = constants.LIBRARY[random.randrange(0,len(constants.LIBRARY))]
            word = Word(text,location,velocity)
            self._words.append(word)
        
        for word in self._words:
            print(word.getWord())

director = Director()
