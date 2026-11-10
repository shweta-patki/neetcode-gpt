import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        m = np.max(z)
        z = z-m
        e = math.e
        s1 = e**z
        s2 = np.sum(s1)
        s = s1/s2
        return np.round(s, 4)
