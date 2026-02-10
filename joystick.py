# i happen to make a similar thing not long ago:
import pygame
from constants import PS5MAP
pygame.init()
pygame.joystick.init()
class ButtonNotFound(Exception):
    """Raises when the button is not found"""
    pass
class AxisNotFound(Exception):
    """Raises when the axis is not found"""
    pass
class Joystick:
    def __init__(self, deviceNumber = 0,map = PS5MAP, deadzone = 8) -> None:
        self.__deviceNumber = deviceNumber
        self.__axis_dict = {}
        self.__button_dict = {}
        self.__map = map
        self.__deadzone = deadzone #  Fight stickdrift
        self.__initiate()
    def __initiate(self): # Initiate the joystick
        self.__joystick = pygame.joystick.Joystick(self.__deviceNumber)
        self.__joystick.init()
    def update(self): 
        pygame.event.pump()
        # PS5:
        for axis in self.__axis_dict:
            self.__axis_dict[axis] = self.__joystick.get_axis(self.__map[axis])
        for button in self.__button_dict:
            self.__button_dict[button] = self.__joystick.get_button(self.__map[button])

    # QOL:
    def set_deadzone(self,deadzone):
        self.__deadzone = deadzone 
    def set_map(self, map):
        self.__map = map
    # Buttons and axes:

    def add_button(self,buttons):
        if isinstance(buttons, str):
            buttons = [buttons]
        for button in buttons:
            if button not in self.__map:
                raise ButtonNotFound
            self.__button_dict[button] = 0

    def add_axis(self,axes):
        if isinstance(axes, str):
            axes = [axes]
        for axis in axes:
            if axis not in self.__map:
                raise AxisNotFound
            self.__axis_dict[axis] = 0

    
    
    # Get data from joystick
    def get_button(self, button):
        return self.__button_dict[button]
    def get_axis(self, axis):
        axisValue = self.__axis_dict[axis]*100 
        return axisValue if abs(axisValue)-self.__deadzone > 0 else 0 
    
"""
# Example: 
js = Joystick()

js.add_button(["RECT","TRI"])
js.add_axis("JSRX")

while 1:
    js.update()
    print(js.get_axis("JSRX"),js.get_button("RECT"), js.get_button("TRI"))
"""