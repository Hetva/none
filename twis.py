data = {
    1: [3, 4, 5],
    2: [6, 8],
    3: [9, 10],
    5: [78, 99],
    6: [12],
    10: [14, 7],
    25: [33],
    89: [25, 26]
}

visited = set()

def dfs(visited, key, data):#key=1
    if key not in visited:#key not in 1
        visited.add(key)#set=1
        print(key, end=" ")

        if key in data:#1
            for value in data[key]:#1[3,4,5]
                # print(value)
                dfs(visited, value, data)#value=3


for key in sorted(data.keys()):#key=1
    dfs(visited, key, data)#key=1
