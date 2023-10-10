def is_invalid_move(row, col, lab):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return True
    if lab[row][col] == "*":
        return True
    if lab[row][col] == "V":
        return True

    return False


def find_exit(row, col, lab, direction, paths):
    if is_invalid_move(row, col, lab):
        return

    paths.append(direction)

    if lab[row][col] == "e":
        print(*paths, sep="")
    else:
        lab[row][col] = "V"
        find_exit(row - 1, col, lab, "U", paths)
        find_exit(row + 1, col, lab, "D", paths)
        find_exit(row, col - 1, lab, "L", paths)
        find_exit(row, col + 1, lab, "R", paths)
        lab[row][col] = "-"

    paths.pop()


rows = int(input())
cols = int(input())
lab = [list(input()) for _ in range(rows)]
find_exit(0, 0, lab, "", [])

"""
3
5
-**-e
-----
*****
"""
