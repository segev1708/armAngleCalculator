from math import asin, acos # import trigonometric functions
from math import degrees # import functions to convert between degrees and radians

class ArmOutOfReachError(Exception):
    """Cannot reach the target! Arm is too short!"""
    pass

def get_angle_laws_of_cosine(a:float ,b:float, c:float):
    # laws of cosine
    angle_c = acos((a**2 + b**2 - c**2) / (2*a*b))
    return degrees(angle_c)  

def ik_calculator_2d(lower_size: float,
                               higher_size: float,
                               target: tuple[float, float]) -> tuple[float, float]:
    """
    Docstring for ik_calculator_2d\n
    Calculates degrees lower and higher servos needs to be for arm's tip to be at-
    target(x,y) if lower part size is lower_size and higher part size is higher_size .
\n
    Check example.png for easy explanation.
\n   
    Key assumptions:
    Servos turn clockwise. 
    All servos 0 degree is with the x axis.
    All servos are 180 degrees.
    x, y are positive:\n
       This function is made to be combined into a bigger one.
       The bigger function handles the third axis by turning the hand to the desired angle like a-
       head turning right and left(360 servo).
       This way we make the 3 dimentional problem into 1 dimentional problem + 2 dimentional problem.
\n
    :param lower_size: Lower part size.
    :type lower_size: float
    :param higher_size: Higher part size.
    :type higher_size: float
    :param target: Target tip (x,y)
    :type target: tuple[float, float]
    """
    
    x, y = target[0], target[1]
    
    distance = (x**2 + y**2) ** 0.5
    if distance > higher_size + lower_size: 
        raise ArmOutOfReachError
    alpha = degrees(asin(y / distance))
    higher_servo_angle = get_angle_laws_of_cosine(lower_size,
                                                  higher_size,
                                                  distance)
    A_degree =  get_angle_laws_of_cosine(lower_size,
                                         distance,
                                         higher_size)
    lower_servo_angle = A_degree + alpha
    return lower_servo_angle, higher_servo_angle



