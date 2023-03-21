import numpy as np
import math


# GRADED FUNCTION: compute_BCE_cost

def compute_BCE_cost(AL, Y):
    """
    Implement the binary cross-entropy cost function using the above formula.

    Arguments:
    AL -- probability vector corresponding to your label predictions, shape (1, number of examples)
    Y -- true "label" vector (for example: containing 0 if non-cat, 1 if cat), shape (1, number of examples)

    Returns:
    cost -- binary cross-entropy cost
    """
    
    m = Y.shape[1]

    # Compute loss from aL and y.
    ### START CODE HERE ### (≈ 1 line of code)
    ϵ = 1e-5
    cost = 0
    for i in range(0,m,1):
        cost = cost + Y[0][i]*math.log(AL[0][i]+ϵ)+(1-Y[0][i])*math.log(1-AL[0][i]+ϵ)
    cost = cost * -1 /m
    ### END CODE HERE ###
    
    cost = np.squeeze(cost)      # To make sure your cost's shape is what we expect (e.g. this turns [[17]] into 17).
    assert(cost.shape == ())
    
    return cost

# GRADED FUNCTION: compute_CCE_cost

def compute_CCE_cost(AL, Y):
    """
    Implement the categorical cross-entropy cost function using the above formula.

    Arguments:
    AL -- probability vector corresponding to your label predictions, shape (number of classes, number of examples)
    Y -- true "label" vector (one hot vector, for example: [[1], [0], [0]] represents rock, [[0], [1], [0]] represents paper, [[0], [0], [1]] represents scissors 
                              in a Rock-Paper-Scissors image classification), shape (number of classes, number of examples)

    Returns:
    cost -- categorical cross-entropy cost
    """
    
    m = Y.shape[1]
    n = Y.shape[0]

    # Compute loss from aL and y.
    ### START CODE HERE ### (≈ 1 line of code)
    ϵ = 1e-5
    cost = 0
    [column[1] for column in A]
    
    for i in range(m):
        for j in range(n):
            cost = cost + Y[j][i]*math.log(AL[j][i]+ϵ)
    cost = cost * -1 /m
    ### END CODE HERE ###
    
    cost = np.squeeze(cost)      # To make sure your cost's shape is what we expect (e.g. this turns [[17]] into 17).
    assert(cost.shape == ())
    
    return cost


