import math
import pygame 
import random
pygame.init()

#iterates through the values of a circle 
_end = False


def random_color() ->tuple[int, int, int]:
    return random.randint(0,255), random.randint(0,255),random.randint(0,255)

class circle:
    def __init__(self, origin :tuple[int,int], radius : int) -> None:
        self.origin = origin
        self.radius = radius

        self.radians  = 0
    def __next__(self, rate :float) ->tuple[int, int]:
        print(self.radians)
        self.radians +=rate
        if self.radians > 2*math.pi:
            self.radians = rate/2
        return int(self.origin[0] + (math.cos(self.radians) * self.radius)) , int(self.origin[1]+ (math.sin(self.radians) * self.radius))
    def set_pos(self, pos : tuple[int,int])->None:
        self.origin = pos
        return 


first_circle = circle((400,400), 100)
#only the first circle's position matters
second_circle = circle((20,20), 50)
third_circle = circle((20,20), 25)
fourth_circle= circle((20,20), 5)
fifth_circle = circle((0,0),1)
if "__main__":
    screen = pygame.display.set_mode((800,800))
    r_color = random_color()
    while _end == False:
        for event in pygame.event.get():
            if event.type  ==pygame.QUIT:
                exit()
        #draw stuff here 
        #first circle rate has to be slower than seconds 
        second_circle.set_pos(first_circle.__next__(0.0001))
        third_circle.set_pos(second_circle.__next__(0.001))
        fourth_circle.set_pos(third_circle.__next__(0.01))
        fifth_circle.set_pos(fourth_circle.__next__(0.1))
        screen.set_at(fifth_circle.__next__(1), r_color)
        
        pygame.display.flip()

