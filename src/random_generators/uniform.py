from typing import Dict

import numpy as np
from scipy import special

from random_generators import RandomGenerator


class UniformGenerator(RandomGenerator):
    @staticmethod
    def generate(low: float = 0.0, high: float = 100.0, sample_size: int = 1000, **kwargs) -> np.ndarray:
        return np.random.uniform(low=low, high=high, size=sample_size)
