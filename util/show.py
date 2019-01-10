import numpy as np

array = np.load('../output.npy')
print(len(array))
for w in array:
    print(w)
    exit()
