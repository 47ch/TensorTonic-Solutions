def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here

    Y = []

    for i in range(len(X)):
        Y.append([])
        for j in range(len(b)):
            Y[i].append([])
            total = 0
            for k in range(len(X[0])):
                total += X[i][k]*W[k][j]

            Y[i][j] = total + b[j]
            
    return Y