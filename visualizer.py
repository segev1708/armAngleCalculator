import pygame
from ik_calculator_2d import ik_calculator_2d as ik2d
from ik_calculator_2d import TargetTooClose, TargetTooFar
from joystick import Joystick
from math import sin, cos, radians, atan2, degrees
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
higher_size = 100
lower_size = 330
target = [200,1000-200]
controller.set_deadzone(17)
offset = 330
target[0] += offset

def draw_dashed_line(display, color, start, end, dash_lenght=10, space = 5, width = 1):
    """Draws a dashed line for better visuals"""
    x1 ,y1 = start
    x2, y2 = end
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    angle = atan2(y2-y1, x2-x1)

    current_distance = 0
    while current_distance < distance:
        dash_end_distance = min(current_distance + dash_lenght, distance)
        start_dash = (x1 + current_distance * cos(angle), y1 + current_distance * sin(angle))
        end_dash = (x1 + dash_end_distance * cos(angle), y1 + dash_end_distance * sin(angle))

        pygame.draw.line(display, color, start_dash, end_dash,width)
        current_distance += dash_lenght + space
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
    except (TargetTooFar, TargetTooClose) as e:
        is_far = isinstance(e, TargetTooFar)
        error_type = "far" if is_far else "close"
        print(f"cant reach: Too {error_type}!" )
        reach = lower_size + higher_size if is_far else abs(lower_size - higher_size)        
        hsa = 180 if is_far else 0
        
        math_x = target[0] - offset
        math_y = 1000 - target[1]

        angle_to_target = atan2(math_y,math_x)
        lsa = degrees(angle_to_target)
        if not is_far and higher_size > lower_size:
            lsa += 180
        target = (offset + cos(angle_to_target)*reach ,
                   1000 - sin(angle_to_target)*reach)
   

    pygame.draw.circle(display,(255,0,0),(target[0],target[1]),5,5)
    draw_dashed_line(display,(255,255,255),(offset,1000),target,10,10,4)
    second_arm_angle = lsa - (180 - hsa)
    middle_x = offset+ lower_size * cos(radians(lsa)) 
    middle_y = 1000 - lower_size * sin(radians(lsa)) 
    top_x = middle_x + higher_size * cos(radians(second_arm_angle))
    top_y = middle_y - higher_size * sin(radians(second_arm_angle))

    
    pygame.draw.line(display, (124, 0, 0), (offset, 1000), (middle_x, middle_y), 5)
    pygame.draw.line(display, (0, 124, 0), (middle_x, middle_y), (top_x, top_y), 5)
    
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
