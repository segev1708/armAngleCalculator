from ik_calculator_2d import ik_calculator_2d as ik2d
from ik_calculator_2d import ArmOutOfReachError 
from math import atan2, degrees
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

    :param lower_size: Description
    :type lower_size: float
    :param higher_size: Description
    :type higher_size: float
    :param target: Description
    :type target: tuple[float, float, float]
    :param turn_speed: Description
    :param balance_point: Description
    """
    directon = round(balance_point + target[2]*turn_speed)
    directon = 0 if directon < 0 else directon
    directon = 180 if directon > 180 else directon 
    try: 
        lsa, hsa = ik2d(lower_size,
                        higher_size,
                        (target[0], target[1]))
    except ArmOutOfReachError:
        hsa = 180
        lsa = degrees(atan2(target[1],target[0]))

    return (lsa, hsa, directon)
