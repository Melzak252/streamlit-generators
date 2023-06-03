import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from numpy import sqrt

from random_generators import RandomGenerator
from numpy.random import random


class UniformRandomGenerator(RandomGenerator):

    def __init__(self, minimum: float = 0, maximum: float = 100):
        if minimum == maximum:
            raise ValueError("Minimum and maximum cannot equals!")

        if minimum > maximum:
            maximum, minimum = minimum, maximum

        self._max: float = maximum
        self._min: float = minimum

    @property
    def d(self):
        return self._max - self._min

    def generate(self, *args, **kwargs) -> float:
        return random() * (self._max - self._min) + self._min

    def set_generator_parameters(self, minimum: float, maximum: float, *args, **kwargs):
        self._max = maximum
        self._min = minimum

    def inverse_density_function(self, x: float, *args, **kwargs) -> float:
        return x


class LinearRandomGenerator(UniformRandomGenerator):

    def __init__(self, minimum: float = 0, maximum: float = 1., alpha: float = 2):
        super().__init__(minimum, maximum)
        self._a = alpha
        self._b = (2 - self._a * self.d * self.d) / (2 * self.d)

        self.validate_density_function()

    def validate_density_function(self):
        if abs(self.d * self.a) > 1 or self.d * self.d * self.a > 2:
            raise ValueError("Cannot define distribution based on given parameters: |d * a| > 1 or d^2 * a > 2")

        if self.b + self.a * self.d > 1:
            raise ValueError("Cannot define distribution based on given parameters: b + a * d > 1")

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def min_x(self):
        return self._min

    @property
    def max_x(self):
        return self._max

    def density_function(self, x: float):
        return self.a * x + self.b

    def distribution_function(self, x: float):
        return self.a * x * x / 2 + self.b * x

    def generate(self, *args, **kwargs) -> float:
        ran = random()
        return ran, self.inverse_distribution_function(ran)

    def inverse_distribution_function(self, x: float, *args, **kwargs) -> float:
        if not self.a:
            return x

        # return (x - self._beta) / self._alpha
        return (-self.b + sqrt(self.b * self.b + 2 * self.a * x)) / self.a

    def inverse_density_function(self, x: float, *args, **kwargs) -> float:
        if not self.a:
            return x

        # return (x - self._beta) / self._alpha
        return (x - self.b) / self.a

    def get_string_parameters(self):
        return f"{self.a = } {self.b = } {self.min = } {self.max = }"

    def get_line(self):
        return self._a, self._b
