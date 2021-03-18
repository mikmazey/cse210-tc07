from game.actor import Actor

class Word(Actor):
    def __init__(self, word, position, velocity):
        super().__init__()
        self.set_text(word)
        self.set_position(position)
        self.set_velocity(velocity)
    
    def getWord(self):
        return self._text

    def setWord(self, word):
        self.set_text(word)