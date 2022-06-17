
    counter = int(input())

    current_maze = list()

    for _ in range(counter):

        data = input()

        current_maze.append(data)

    escape(current_maze)

maze()
