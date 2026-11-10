import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z = 1 / (1+ (math.e)**(-z))
        return np.round(z, 5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z = np.maximum(0, z)
        return z
