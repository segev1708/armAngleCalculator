import pygame
from ik_calculator_2d import ik_calculator_2d as ik2d
from ik_calculator_2d import ArmOutOfReachError
from joystick import Joystick
from math import sin, cos, radians
display = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
fps = 60
running = True
controller = Joystick()

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
lower_size = 250
higher_size = 330
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
        lsa, hsa = ik2d(lower_size, higher_size, (target[0]-offset, (1000)-target[1]))
    except ArmOutOfReachError:
        print("cant reach!")
        target = (target[0] - (0.12 * controller.get_axis("JSRX")),
                  target[1] - (0.12 * controller.get_axis("JSRY")))
        continue
    
    # print(lsa,hsa)

    pygame.draw.circle(display,(255,0,0),(target[0],target[1]),5,5)
    pygame.draw.line(display,(0,0,128),(offset,1000),target,4)

    second_arm_angle = lsa - (180 - hsa)
    middle_x = offset+ lower_size * cos(radians(lsa)) 
    middle_y = 1000 - lower_size * sin(radians(lsa)) 
    top_x = middle_x + higher_size * cos(radians(second_arm_angle))
    top_y = middle_y - higher_size * sin(radians(second_arm_angle))

    if target[0] < offset: # Making it less buggy on negative - not meant to really happen but it is a thing to prevent weird glitching.
        middle_x = offset - abs(offset - middle_x )
        top_x = offset - abs(offset - top_x )

    pygame.draw.line(display, (0, 0, 0), (offset, 1000), (middle_x, middle_y), 5)
    pygame.draw.line(display, (0, 0, 0), (middle_x, middle_y), (top_x, top_y), 5)
    
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
