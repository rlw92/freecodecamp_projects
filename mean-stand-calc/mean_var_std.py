import numpy as np

def calculate(list):

 arr = np.array(list)

 if arr.size < 9:
    raise ValueError("List must contain nine numbers.")
 else:  
    matrix = arr.reshape(3,3)

#mean
    mean0 = np.mean(matrix, axis=0)
    mean1 = np.mean(matrix, axis=1)
    flatMean= np.mean(arr)
#var
    var0 = np.var(matrix, axis=0)
    var1 = np.var(matrix, axis=1)
    flatVar= np.var(arr)
#std
    std0 = np.std(matrix, axis=0)
    std1 = np.std(matrix, axis=1)
    flatStd= np.std(arr)
#max
    max0 = np.max(matrix, axis=0)
    max1 = np.max(matrix, axis=1)
    flatMax= np.max(arr)
#min
    min0 = np.min(matrix, axis=0)
    min1 = np.min(matrix, axis=1)
    flatMin= np.min(arr)
#sum
    sum0 = np.sum(matrix, axis=0)
    sum1 = np.sum(matrix, axis=1)
    flatSum= np.sum(arr)
    
    calculations = {
       'mean': [mean0.tolist(),mean1.tolist(),flatMean],
       'variance': [var0.tolist(),var1.tolist(),flatVar],
       'standard deviation': [std0.tolist(),std1.tolist(),flatStd],
       'max': [max0.tolist(),max1.tolist(),flatMax],
       'min': [min0.tolist(),min1.tolist(),flatMin],
       'sum': [sum0.tolist(),sum1.tolist(),flatSum]
      
       
           }




    return calculations