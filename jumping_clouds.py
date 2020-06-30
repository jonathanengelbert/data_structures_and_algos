def jumpingClouds(c):
    total = len(c)
    valid_path = []
    shortest_path = []

    index = 0
    # make valid path
    for cloud in c:
        if cloud == 0:
            valid_path.append(index)
        index += 1

    current_cloud_index = 0
    shortest_path.append(valid_path[0])
    print("VALID PATH:", valid_path)
    for i, cloud in enumerate(valid_path):
        if i >= current_cloud_index:
            # is there a cloud two clouds away? is its value within two numbers of current_cloud?
            if i + 2 < len(valid_path) and valid_path[i + 2] <= valid_path[i] + 2:
                next_cloud = valid_path[i + 2]
                shortest_path.append(next_cloud)
                current_cloud_index = i + 2
            elif i + 1 < len(valid_path):
                next_cloud = valid_path[i + 1]
                shortest_path.append(valid_path[i + 1])
                current_cloud_index = i + 1


    print("SHORTEST PATH:", shortest_path)
    print("JUMPS:", len(shortest_path) -1)

# input 0
# jumpingClouds([0, 0, 1, 0, 0, 1, 0])
# input 1
jumpingClouds([0, 0, 0, 0, 1, 0])