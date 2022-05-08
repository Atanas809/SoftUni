def output(standings):
    print("Individual standings:")
    sort_dic = dict()
    for key, value in standings.items():
        points = value[0]
        name = key
        if name not in sort_dic.values():
            sort_dic[name] = points
    nums = sorted(sort_dic.values(), reverse=True)
    counter = 1
    for x in nums:
        for item in sort_dic.items():
            if item[1] == x:
                print(f"{counter}. {item[0]} -> {item[1]}")
                counter += 1
                del sort_dic[item[0]]
                break



def result(my_dict):

    for key, value in my_dict.items():
        print(f"{key}: {len(value) // 2} participants")
        sort_dic = dict()
        for x in range(0, len(value), 2):
            name = value[x]
            points = value[x + 1]
            if name not in sort_dic.values():
                sort_dic[name] = points
        output = sorted(sort_dic.values(), reverse=True)
        counter = 1
        for y in output:
            for item in sort_dic.items():
                if item[1] == y:
                    print(f"{counter}. {item[0]} <::> {item[1]}")
                    counter += 1
                    del sort_dic[item[0]]
                    break




