"CSCI 630 FIS Assignment 1"
__author__ = "Uddesh Karda"
from vertex import *
import sys
import heapq
import math

puzzle_matrix = []
queue = []
visited = []


class PriorityQueue:
    """
    Class to implement Priority queue
    """
    def __init__(self):
        """
        INitialization function
        """
        self.elements = []

    def empty(self):
        """
        Function to check if priority queue is empty or not
        :return: Boolean Data
        """
        return len(self.elements) == 0

    def pushIt(self, priority, item):
        """
        Function to push vertex into priority queue
        :param priority: Priority of item
        :param item: Vertex
        :return: -
        """

        heapq.heappush(self.elements, ( priority, item))

    def get(self):
        """
        Function to pop vertex from priority queue
        :return: vertex object
        """
        return heapq.heappop(self.elements)[1]

def heuristic(p, q):
    """
    Heuristic calculation by Manhattan distance
    :param p: co-ordinates of current node
    :param q: co-ordinates of goal node
    :return: heuristic distance h to goal node
    """
    (x1, y1) = p
    (x2, y2) = q
    return abs(x1 - x2) + abs(y1 - y2)

def heuristic2(p, q):
    """
    Heuristic calculation by Diagonal distance
    :param p: co-ordinates of current node
    :param q: co-ordinates of goal node
    :return: heuristic distance h to goal node
    """
    (x1, y1) = p
    (x2, y2) = q
    h = max(abs(x1 - x2), abs(y1 - y2))
    return h

def heuristic3(p, q):
    """
    Heuristic calculation by Euclidean distance
    :param p: co-ordinates of current node
    :param q: co-ordinates of goal node
    :return: heuristic distance h to goal node
    """
    (x1, y1) = p
    (x2, y2) = q
    h = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 -y2), 2))
    return h

def heuristic4(p, q):
    """
    Heuristic calculation
    :param p: co-ordinates of current node
    :param q: co-ordinates of goal node
    :return: Zero
    """
    return 0

def astar(graph, start, goal):
    """
    Runs A* algorithm on a given graph
    :param graph: List of list of data in file
    :param start: Start node
    :param goal: Goal node
    :return: -
    """
    for x in range(len(puzzle_matrix)):
        col = []
        for y in range(len(puzzle_matrix[0])):
            col.append(False)
        visited.append(col)

    steps = 0
    depth = 0
    if puzzle_matrix[0][0] != str(1):
        if start is None:
            start = vertex(0, 0, 0)
    else:
        sys.exit("No soluiton")

    pq = PriorityQueue()
    pq.pushIt(0, start)
    visited[0][0] = True

    goal_x = len(puzzle_matrix) - 1
    goal_y = len(puzzle_matrix[0]) - 1

    while not pq.empty():
        currentNode = pq.get()
        steps += 1
        currentNode_x = currentNode.x
        currentNode_y = currentNode.y

        if currentNode_x == goal_x and currentNode_y == goal_y:
            print(currentNode_x, currentNode_y)
            print(steps)
            print(currentNode)
            break

        if  currentNode_x + 1 < len(puzzle_matrix):
            if visited[currentNode_x + 1][currentNode_y] == False and puzzle_matrix[currentNode_x + 1][currentNode_y] != str(1):
                v = vertex(currentNode_x+1, currentNode_y,
                                 heuristic3((currentNode_x + 1, currentNode_y), (goal_x, goal_y)))
                v.parent_x = currentNode_x
                v.parent_y = currentNode_y

                pq.pushIt((currentNode_x + 1 + currentNode_y + heuristic3((currentNode_x + 1, currentNode_y), (goal_x, goal_y))),v)
                visited[currentNode_x + 1][currentNode_y] = True

        if currentNode_y + 1 < len(puzzle_matrix[0]):
            if visited[currentNode_x][currentNode_y+1]==False  and puzzle_matrix[currentNode_x][currentNode_y + 1] != str(1):
                v = vertex(currentNode_x , currentNode_y+1,
                           heuristic3((currentNode_x, currentNode_y+1), (goal_x, goal_y)))
                v.parent_x = currentNode_x
                v.parent_y = currentNode_y

                pq.pushIt((currentNode_x  + currentNode_y + 1 + heuristic3((currentNode_x , currentNode_y + 1), (goal_x, goal_y))),v)
                visited[currentNode_x][currentNode_y + 1] = True

        if currentNode_x - 1 >= 0:
            if visited[currentNode_x - 1][currentNode_y]==False and puzzle_matrix[currentNode_x-1][currentNode_y] != str(1):
                v = vertex(currentNode_x - 1, currentNode_y ,
                           heuristic3((currentNode_x -1 , currentNode_y ), (goal_x, goal_y)))
                v.parent_x = currentNode_x
                v.parent_y = currentNode_y

                pq.pushIt((currentNode_x - 1 + currentNode_y  + heuristic3((currentNode_x - 1, currentNode_y ),
                                                                         (goal_x, goal_y))), v)
                visited[currentNode_x - 1][currentNode_y] = True

        if currentNode_y - 1 >= 0:
            if visited[currentNode_x][currentNode_y - 1] == False and puzzle_matrix[currentNode_x ][currentNode_y-1] != str(1):
                v = vertex(currentNode_x , currentNode_y - 1,
                           heuristic3((currentNode_x , currentNode_y -1), (goal_x, goal_y)))
                v.parent_x = currentNode_x
                v.parent_y = currentNode_y

                pq.pushIt((currentNode_x + currentNode_y - 1 + heuristic3((currentNode_x, currentNode_y -1),(goal_x, goal_y))), v)
                visited[currentNode_x][currentNode_y - 1] = True

        print(currentNode_x, currentNode_y)

def main():
    """
    Main function
    :return: -
    """
    with open("1") as puzzle:
        for line in puzzle:
            vertices_in_row = line.split(" ")
            puzzle_matrix.append(vertices_in_row)

    astar(puzzle_matrix, None, None)

if __name__ == '__main__':
    main()

