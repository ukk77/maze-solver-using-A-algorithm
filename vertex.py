"CSCI 630 FIS Assignment 1"
__author__ = "Uddesh Karda"

class vertex:
    """
    Vertex class to implement vertex object
    """
    __slots__ = 'x', 'y', 'f', 'g', 'h', 'parent_x', 'parent_y'

    def __init__(self, x, y, h):
        """
        Initialization function
        :param x: Co-ordinate x of current node
        :param y: Co-ordinate y of current node
        :param h: Heuristic estimate of current node
        """
        self.x = x
        self.y = y
        self.h = h
        self.g = self.x + self.y
        self.f = self.g + self.h
        self.parent_x = None
        self.parent_y = None


    def __str__(self):
        """
        Str function of node
        :return: String representation of node
        """
        return f"({self.x},{self.y}) g-{self.g} h-{self.h} f-{self.f} "

    def __lt__(self, other):
        """
        Function to compare the heuristic priority of two vertices
        :param other: Other vertex object
        :return: Object with higher priority
        """
        return self.f < other.f