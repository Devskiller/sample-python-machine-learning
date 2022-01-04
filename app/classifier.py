import numpy as np


class Classifier:
    def __init__(self, normal: np.ndarray, translation: np.ndarray):
        self._normal = normal
        self._translation = translation

    def classify(self, point: np.ndarray) -> bool:
        return True
