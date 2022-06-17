def escape(current_maze):

    for x in range(len(current_maze)):
        if "k" in current_maze[x]:
            index = current_maze[x].index("k")



def maze():

    counter = int(input())

    current_maze = list()

    for _ in range(counter):

        data = input()

        current_maze.append(data)

    escape(current_maze)

maze()