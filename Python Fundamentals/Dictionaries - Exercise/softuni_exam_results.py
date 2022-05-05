def submissions(result):

    print("Submissions:")

    for course, values in result.items():
        print(f"{course} - {len(values) // 2}")

def output(result):
    print("Results:")

    for key, value in result.items():
        for x in range(0, len(value), 2):
            name = value[x]
            points = value[x + 1]
            if name != "already in" and name != "banned":
                print(f"{name} | {points}")

    submissions(result)

def exam_results():

    command = input().split("-")

    results = dict()

    while command[0] != "exam finished":

        if command[1] == "banned":
            name = command[0]

            for key, value in results.items():
                if name in value:
                    for i in range(0, len(value), 2):
                        if value[i] == name:
                            results[key][i] = "banned"

        else:
            name = command[0]
            course = command[1]
            points = int(command[2])

            if course not in results.keys():
                results[course] = list()
                results[course].append(name)
                results[course].append(points)

            else:
                if name in results[course]:
                    index = results[course].index(name)

                    if results[course][index + 1] < points:
                        results[course][index + 1] = points

                    results[course].append("already in")
                    results[course].append(points)

                else:
                    results[course].append(name)
                    results[course].append(points)

        command = input().split("-")

    output(results)

exam_results()

