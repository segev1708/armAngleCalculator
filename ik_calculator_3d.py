from ik_calculator_2d import ik_calculator_2d as ik2d
from ik_calculator_2d import TargetTooClose, TargetTooFar 
from math import atan2, degrees

# BETA
def ik_calculator_3d(lower_size: float,
                               higher_size: float,
                               target: tuple[float, float, float],
                               turn_speed: float,
                               balance_point : float = 90) -> tuple[float, float, int]:
    """
    Docstring for ik_calculator_3d
    Uses ik_calculator_2d to calculate lower and higher servos required degrees. but also calculates base servo.
    Please read Docstring for ik_calculator_2d for farther explanation.

\n

    :param lower_size: Size of the lower part of the arm
    :type lower_size: float
    :param higher_size: Size of the higher part of the arm
    :type higher_size: float
    :param target: Target (x, y ,z) while x,y are on the 2D plane of the arm itself and z is how much the plane needs to move relatively to its current position.
    :type target: tuple[float, float, float]
    :param turn_speed: Turn speed, how fast should the arm try to move
    :param balance_point: Balance point of the 360 servo which turns the arm. (should be near 90)
    """
    directon = round(balance_point + target[2]*turn_speed)
    directon = 0 if directon < 0 else directon
    directon = 180 if directon > 180 else directon 
    try: 
        lsa, hsa = ik2d(lower_size,
                        higher_size,
                        (target[0], target[1]))
    except TargetTooFar:
        hsa = 180
        lsa = degrees(atan2(target[1],target[0]))
    except TargetTooClose:
        hsa = 0
        lsa = degrees(atan2(target[1],target[0]))

    return (lsa, hsa, directon)
