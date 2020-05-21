import playsound
import pygame

# playsound method 
def playsound_method():
    for i in range(10):
        playsound.playsound('../data/warning.wav', True)
        print(i)


class PlaySound:
    def __init__(self):
        pygame.mixer.init()
        self.soundwav = pygame.mixer.Sound('../data/warning.wav')
     
    def play(self):
        while 1:
            print('1')
            if not pygame.mixer.music.get_busy():
                self.soundwav.play()
                pygame.time.delay(1000)

#playsound_method()

play = PlaySound()
play.play()
