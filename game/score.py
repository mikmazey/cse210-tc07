class Score:
    def __init__(self):
        self._score = 0
    
    def setScore(self, score):
        self._score = score
    
    def getScore(self):
        return self._score

    def changeScore(self, change):
        self._score += int(change)
