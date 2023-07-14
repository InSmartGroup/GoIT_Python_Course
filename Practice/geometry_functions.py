def line_segment_length(point_1: int or float, point_2: int or float):
    """
    :param point_1: Point 1 of the line segment
    :param point_2: Point 2 of the line segment
    :type point_1: int or float
    :type point_2: int or float
    :return: The length of the line segment
    :rtype: int or float
    """
    try:
        return abs(point_2 - point_1)
    except TypeError:
        return "Both arguments should be numeric type"


def line_slope(x1: int or float, y1: int or float, x2: int or float, y2: int or float):
    """
    :param x1: Point 1 coordinate on the 'x' axis
    :param y1: Point 1 coordinate on the 'y' axis
    :param x2: Point 2 coordinate on the 'x' axis
    :param y2: Point 2 coordinate on the 'y' axis
    :type x1: int or float
    :type y1: int or float
    :type x2: int or float
    :type y2: int or float
    :return: The slope of the line
    :rtype: float
    """
    try:
        return (y2 - y1) / (x2 - x1)
    except TypeError:
        return "All arguments should be numeric type"


def line_midpoint(x1: int or float, y1: int or float, x2: int or float, y2: int or float):
    """
    :param x1: Point 1 coordinate on the 'x' axis
    :param y1: Point 1 coordinate on the 'y' axis
    :param x2: Point 2 coordinate on the 'x' axis
    :param y2: Point 2 coordinate on the 'y' axis
    :type x1: int or float
    :type y1: int or float
    :type x2: int or float
    :type y2: int or float
    :return: The line midpoint 'x' and 'y' axes coordinates
    :rtype: float
    """
    try:
        return (x1 + x2) / 2, (y1 + y2) / 2
    except TypeError:
        return "All arguments should be numeric type"

