from game.word import Word
from game.buffer import Buffer
from game.inputService import InputService
from game.outputService import OutputService
from game.score import Score
from game.actor import Actor
from game import constants
import random
from game.point import Point
from time import sleep

class Director:
    def __init__(self,inputService,outputService):
        self._words = []
        self._buffer = Buffer()
        self._inputService = inputService
        self._outputService = outputService
        self._score = Score()

        for i in range(5):
            location = Point(random.randrange(0,40),random.randrange(1,19))
            velocity = Point(random.randrange(1,5),0)
            text = constants.LIBRARY[random.randrange(0,len(constants.LIBRARY))]
            word = Word(text,location,velocity)
            self._words.append(word)

    def startGame(self):
        while True:
            self._getInputs()
            self._doUpdates()
            self._doOutputs()
            sleep(constants.FRAME_LENGTH)

    def _getInputs(self):
        letter = self._inputService.get_letter()
        if letter == "*":
            self._buffer.clearBuffer()
        elif letter == "backspace":
            self._buffer.pop()
        else:
            self._buffer.push(letter)

    def _doUpdates(self):
        for word in self._words:
            word.move_next()
            pos = word.get_position()
            if self._buffer.isInBuffer(word.getWord()) or pos.get_x() > constants.MAX_X:
                self._words.remove(word)
                location = Point(0,random.randrange(1,19))
                velocity = Point(random.randrange(1,3),0)
                text = constants.LIBRARY[random.randrange(0,len(constants.LIBRARY))]
                self._words.append(Word(text,location,velocity))
            if self._buffer.isInBuffer(word.getWord()):
                self._score.changeScore(1)

    def _doOutputs(self):
        self._outputService.clear_screen()
        scoreText = Word("Score: " + str(self._score.getScore()),Point(0,0),Point(0,0))
        bufferText = Word(self._buffer.toString(),Point(0,20),Point(0,0))
        self._outputService.draw_actor(scoreText)
        self._outputService.draw_actor(bufferText)
        for word in self._words:
            self._outputService.draw_actor(word)
        self._outputService.flush_buffer()