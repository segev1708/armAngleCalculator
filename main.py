from math import  sin, cos ,tan, asin, acos, atan # import trigonometric functions
from math import radians, degrees # import functions to convert between degrees and radians

class ArmOutOfReachError(Exception):
    """Cannot reach the target! Arm is too short!"""
    pass

def get_angle_laws_of_cosine(a:float ,b:float, c:float):
    # laws of cosine
    angle_c = acos((a**2+b**2-c**2)/(2*a*b))
    return degrees(angle_c)  
def two_dimentional_calculator(lowerSize: float,
                               higherSize: float,
                               target: tuple[float, float]):
    """
    Docstring for two_dimentional_calculator\n
    Calculates degrees lower and higher servos needs to be for arm's tip to be at-
    target(x,y) if lower part size is lowerSize and higher part size is higherSize .
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
    :param lowerSize: Lower part size.
    :type lowerSize: float
    :param higherSize: Higher part size.
    :type higherSize: float
    :param target: Target tip (x,y)
    :type target: tuple[float, float]
    """
    
    x, y = abs(target[0]), abs(target[1])
    
    distance = (x**2 + y**2) ** 0.5
    if distance > higherSize+ lowerSize: 
        raise ArmOutOfReachError
    alpha = degrees(asin(y / distance))
    higherServoAngle = get_angle_laws_of_cosine(lowerSize,higherSize,distance)
    A =  get_angle_laws_of_cosine(lowerSize,distance,higherSize)
    lowerServoAngle = A+alpha
    return lowerServoAngle,higherServoAngle


print(two_dimentional_calculator(2,2,(1,2)))
