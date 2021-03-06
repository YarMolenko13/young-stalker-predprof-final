import pathfinding
mesages =   [
        {
            "coords": [
                9,
                9
            ],
            "id": 1,
            "swans": [
                {
                    "id": "8518f426",
                    "rate": 0.1134
                },
                {
                    "id": "e2786bef",
                    "rate": 0.1038
                },
                {
                    "id": "7cae2c6d",
                    "rate": 0.35
                },
                {
                    "id": "699a7e76",
                    "rate": 1.0938
                },
                {
                    "id": "8f198b5e",
                    "rate": 0.4575
                }
            ]
        },
        {
            "coords": [
                33,
                8
            ],
            "id": 2,
            "swans": [
                {
                    "id": "b44650d9",
                    "rate": 0.6931
                },
                {
                    "id": "8518f426",
                    "rate": 5.0
                },
                {
                    "id": "e2786bef",
                    "rate": 0.9231
                },
                {
                    "id": "7cae2c6d",
                    "rate": 0.2208
                },
                {
                    "id": "699a7e76",
                    "rate": 0.1065
                },
                {
                    "id": "8f198b5e",
                    "rate": 0.1148
                }
            ]
        },
        {
            "coords": [
                9,
                22
            ],
            "id": 3,
            "swans": [
                {
                    "id": "b44650d9",
                    "rate": 0.1092
                },
                {
                    "id": "e2786bef",
                    "rate": 0.1062
                },
                {
                    "id": "7cae2c6d",
                    "rate": 0.6422
                },
                {
                    "id": "699a7e76",
                    "rate": 2.8
                },
                {
                    "id": "8f198b5e",
                    "rate": 7.0
                }
            ]
        },
        {
            "coords": [
                33,
                23
            ],
            "id": 4,
            "swans": [
                {
                    "id": "b44650d9",
                    "rate": 2.6923
                },
                {
                    "id": "8518f426",
                    "rate": 0.2439
                },
                {
                    "id": "e2786bef",
                    "rate": 1.2
                },
                {
                    "id": "7cae2c6d",
                    "rate": 0.3302
                },
                {
                    "id": "699a7e76",
                    "rate": 0.1144
                },
                {
                    "id": "8f198b5e",
                    "rate": 0.1573
                }
            ]
        }
    ]
maze = []
for i in range(30):
    maze.append([])
    for j in range(40):
        maze[i].append(0)

anomalies = []
ides = set()

for i in mesages:
    for swan in i["swans"]:
        ides.add(swan["id"])
ides = list(ides)
for anom_name in ides:
    for i in range(30):
        for j in range(40):
            past_values = []
            for anom in mesages:
                coord = anom["coords"]
                for swan in anom["swans"]:
                    if swan["id"] == anom_name:
                        past_values.append([swan["rate"], coord])

            test_value = (((past_values[0][1][0] - j) ** 2) + ((past_values[0][1][1] - i) ** 2)) * past_values[0][0]
            for c_anomaly in past_values[1:]:
                not_test_value = (((c_anomaly[1][0] - j) ** 2) + ((c_anomaly[1][1] - i) ** 2)) * c_anomaly[0]
                if round(not_test_value) != round(test_value):
                    break
            else:
                anomalies.append([j, i, round(test_value)])


for i in range(30):
    for j in range(40):
        for anom in anomalies:
            d = (anom[0] - j) ** 2 + (anom[1] - i) ** 2
            if d == 0:
                maze[i][j] = 2
                continue
            power = anom[2] / d
            if power >= 2:
                maze[i][j] = 1





# PATHFINDING


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def calc_path(a, b):


    start = (0, 0)
    end = (29, 39)

    path = astar(maze, start, end)
    return path


for i in anomalies:
    maze[i[1]][i[0]] = 2
for i in range(30):
    for j in range(40):
        print(maze[i][j], end=" ")
    print()
paths = calc_path(0, 0)
for i in paths:
    maze[i[0]][i[1]] = 3


