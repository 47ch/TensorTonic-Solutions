def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here

    if not points:
        return []
    else:
        dimensionality = len(points[0])

    vector_init = []
    vector_init = [0 for i in range(dimensionality)]
    # for i in range(dimensionality):
    #     vector_init.append(0)

    return_array = [vector_init]*k
    count = 0
    prev = 0

    for i in range(len(assignments)):
        count += 1
        cluster = assignments[i]
        return_array[cluster] = [x + y for x,y in zip(return_array[cluster], points[i])]
        try:
            if cluster != assignments[i+1]:
                return_array[cluster] = [x/(count) for x in return_array[cluster]]
                count = 0
        except:
            return_array[cluster] = [x/(count) for x in return_array[cluster]]

    return return_array