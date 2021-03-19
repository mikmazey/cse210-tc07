from game.director import Director
from game.inputService import InputService
from game.outputService import OutputService
from asciimatics.screen import Screen 

def main(screen):
    input_service = InputService(screen)
    output_service = OutputService(screen)
    director = Director(input_service, output_service)
    director.startGame()

Screen.wrapper(main)