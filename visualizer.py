import pygame
import main, joystick
from math import sin, cos, tan, asin, acos, atan, sqrt, pow, degrees, radians
display = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
fps = 60
running = True
controller = joystick.Joystick()

controller.add_axis(("JSLX",
                     "JSLY",
                     "JSRX",
                     "JSRY",
                     "L2",
                     "R2",
                     )
)
controller.add_button(("X",
        "O",
        "RECT",
        "TRI",
        "TRIANGLE",
        "SHARE",
        "PS",
        "OPTIONS",
        "L3",
        "R3",
        "L1",
        "R1",
        "UP",
        "DOWN",
        "LEFT",
        "RIGHT",
        "PAD",
        "MUTE"))
lowerSize = 250
higherSize = 330
target = [200,1000-200]
controller.set_deadzone(17)
offset = 330
target[0] += offset


while running:
    controller.update()
    display.fill((128, 128, 128))
    target = (target[0] + (0.02 * controller.get_axis("JSRX")),
              target[1] + (0.02 * controller.get_axis("JSRY")))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    try:
        lsa, hsa = main.two_dimentional_calculator(lowerSize,higherSize,(target[0]-offset,(1000)-target[1]))
    except main.ArmOutOfReachError:
        print("cant reach!")
        target = (target[0] - (0.12 * controller.get_axis("JSRX")),
                  target[1] - (0.12 * controller.get_axis("JSRY")))
        continue
    
    # print(lsa,hsa)

    pygame.draw.circle(display,(255,0,0),(target[0],target[1]),5,5)
    pygame.draw.line(display,(0,0,128),(offset,1000),target,4)

    
    middleX = offset+ lowerSize * cos(radians(lsa)) 
    middleY = 1000 - lowerSize * sin(radians(lsa)) 

    second_arm_angle = lsa - (180 - hsa)
    topX = middleX + higherSize * cos(radians(second_arm_angle))
    topY = middleY - higherSize * sin(radians(second_arm_angle))
    if target[0] < offset: # Making it work on negative - not meant to really happen but is a thing
        middleX = offset - abs(offset- middleX )
        topX = offset - abs(offset- topX )
    pygame.draw.line(display, (0,0,0), (offset,1000), ((middleX), middleY), 5)
    pygame.draw.line(display, (0,0,0), (middleX, middleY), (topX,topY), 5)
    pygame.display.update()

    clock.tick(fps)


pygame.quit()
