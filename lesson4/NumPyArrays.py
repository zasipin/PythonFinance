""" creating NumPy arrays """
import numpy as np

def test_run():
    # List to 1D array
    print(np.array([2, 3, 4]))
    # List of tuples to 2D array
    print(np.array([(2, 3, 4), (5, 6, 7)]))
    #Empty array
    print(np.empty(5))
    print(np.empty((5, 4))) # 5 rows 4 cloumns
    #print(np.empty((5, 4, 2))) # 5 rows 4 cloumns 2 depth of array (3 dimentions)

    #Array of 1s
    print(np.ones((5, 4), dtype = np.int_))

    # Generate array of random numbers, uniformly sampled from [0.0, 1.0)
    print(np.random.random((5, 4)))
    print(np.random.rand(5, 4)) # the same

    # Sample numbers from a Gaussian (normal) distribution
    print(np.random.normal(size=(2, 3))) # "standard normal" (mean = 0, standard deviation = 1)
    print(np.random.normal(50, 10, size=(2, 3))) # (mean = 50, standard deviation = 10)

    # Random integers
    print(np.random.randint(10)) # a single intege in [0, 10)
    print(np.random.randint(0, 10)) # same as above, specifiying [low, high) explicit
    print(np.random.randint(0, 10, size = 5)) # 5 random integers as a 1D array
    print(np.random.randint(0, 10, size=(2, 3))) # 2x3 arra y of random integers
    
    # Array attributes
    a = np.random.random((5, 4))
    print(a.shape)      # number of dimensions
    print(len(a.shape))
    print(a.shape[0]) # number of rows
    print(a.shape[1]) # number of columns
    print(a.size)     # number of elements in a
    print(a.dtype)    # dtype of elements

    # Operations on arrays
    np.random.seed(693) # seed the random number generator
    a = np.random.randint(0, 10, size=(5, 4)) # 5x4 random integers in [0, 10)
    print("Array:\n", a)
    print("Sum of all elements:", a.sum())
    # axis = 0 - columns, 1 - rows

    #Iterate over rows, to compute sum of each column
    print("Sum of each column:\n", a.sum(axis=0))
    #Iterate over columns, to compute sum of each row
    print("Sum of each row:\n", a.sum(axis=1))

    # Statistics: min, max, mean(across rows, cols, and overall)
    print("Min of each column:\n", a.min(axis=0))
    print("Max of each row:\n", a.max(axis=1))
    print("Mean of all elements:\n", a.mean())

    
    """ functions
numpy.empty
numpy.ones
numpy.zeros
numpy.array
numpy.ndarray (direct ndarray constructor)
"""

if __name__ == "__main__":
    test_run()
