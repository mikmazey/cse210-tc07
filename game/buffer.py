from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    def __init__(self):
        """
        Initialize the buffer
        """
        super().__init__()
        self._text = ""
        self.set_position(Point(1,constants.MAX_Y))
    
    def push(self, char):
        """
        Adds the given character to the end of the buffer
        """
        self._text += char
    
    def pop(self):
        """
        Removes the last character from the end of the buffer
        """
        self._text = self._text[:-1]
    
    def toString(self):
        """
        Return the buffer string
        """
        return self._text
    
    def clearBuffer(self):
        """
        Clear the buffer
        """
        self._text = ""
    
    def updateBuffer(self, char):
        """
        - If the char is in the alphabet, add the char to the buffer
        - If the string "backspace" is received, then simply call pop()
        - If the '*' character is received, clear the buffer
        """
        if (len(char) == 1 and ord(char) >= 97 and ord(char) <= 122):
            self.push(char)
        elif (char == "backspace"):
            self.pop()
        elif (char == "*"):
            self.clearBuffer()

    def isInBuffer(self, substring):
        """
        Check to see if the given substring is part of the buffer
        """
        return False if self._text.find(substring) == -1 else True