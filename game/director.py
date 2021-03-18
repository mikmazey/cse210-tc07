from word import Word
from buffer import Buffer
from inputService import InputService
from outputService import OutputService
from score import Score
import constants
import random

class Director:
    def __init__():
        self._words = []
        self._buffer = Buffer()
        self._inputService = InputService
        self._outputService = OutputService
        self._score = Score
        self._deathCounter

        for i in range(5):
            word = Word(randrange(0,40),randrange(1,19),randrange(1,5),0)
            self._words += word

    def startGame(self):
        while not self._score.getScore() + _deathCounter == len(self._actors()):
            self._getInputs()
            self._doUpdates()
            self._doOutputs()

    def _getInputs():
        letter = self._inputService.get_letter()
        if letter == "*":
            self._buffer.clearBuffer()
        elif letter == "backspace":
            self._buffer._pop()
        else:
            self._buffer.push(letter)

    def _doUpdates():
        self._score.updateScore(self._words)

        for word in self._words:
            word.update()
            if self._buffer.isInBuffer(word.getWord()):
                self._words.remove(word)
                self._words.append(Word(0,randrange(1,19),randrange(1,5),0))
                self._score.updateScore(1)


    def _doOutputs():
        self._outputService.printScore(self._score.getScore())
        for word in self._words():
            self._outputService.draw_actor(word)
        self._outputService.printBuffer(self._buffer)

