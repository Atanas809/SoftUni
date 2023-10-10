def best_increasing_subsequence(goals):
    n = len(goals)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if goals[i] >= goals[j]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    max_length = max(dp)
    idx = dp.index(max_length)
    best_sequence = []

    while idx != -1:
        best_sequence.append(goals[idx])
        idx = prev[idx]

    best_sequence.reverse()
    return best_sequence


goals_input = input().split(", ")
goals = [int(goal) for goal in goals_input]

best_sequence = best_increasing_subsequence(goals)
print(" ".join(map(str, best_sequence)))


"""
0, 1, 3, 2, 4, 6, 5
2, 2, 1, 5, 4, 6, 7, 3
"""