from typing import Dict

import numpy as np
from scipy import special

from random_generators import RandomGenerator


class NormalGenerator(RandomGenerator):
    @staticmethod
    def generate(mean: float = 100.0, dev: float = 15.0, sample_size: int = 100, **kwargs) -> np.ndarray:
        return np.random.normal(loc=mean, scale=dev, size=sample_size)
