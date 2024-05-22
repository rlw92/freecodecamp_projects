import numpy as np

def calculate(list):

    arr = np.array(list)
    matrix = arr.reshape(3,3)
    mean0 = np.mean(matrix, axis=0)
    mean1 = np.mean(matrix, axis=1)
    flat= np.mean(arr)
    mean= np.stack((mean0, mean1), axis=0)
    
    calculations = {
       'mean': mean,
       'flattened': flat
    }




    return calculations