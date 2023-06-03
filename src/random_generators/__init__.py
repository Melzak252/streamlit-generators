from abc import ABC, abstractmethod, abstractstaticmethod
from dataclasses import dataclass
from typing import Tuple, Dict, List

import numpy as np


class RandomGenerator(ABC):
    @staticmethod
    @abstractmethod
    def generate(sample_size: int = 100, **kwargs) -> np.ndarray:
        pass
