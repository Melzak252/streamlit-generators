import numpy as np
import streamlit as st

from app.generator_pages import GeneratorPage
from random_generators.normal import NormalGenerator
from random_generators.uniform import UniformGenerator


class UniformGeneratorPage(GeneratorPage):
    def get_expected_value(self, x, *args, **kwargs) -> float:
        return self._constant / self.delta

    @property
    def delta(self):
        return st.session_state.min_max[1] - st.session_state.min_max[0]

    def get_values(self) -> np.ndarray:
        low, high = st.session_state.min_max
        return UniformGenerator.generate(
            low=low,
            high=high,
            sample_size=st.session_state.sample_size
        )

    @property
    def _constant(self) -> float:
        return st.session_state.bin_size * st.session_state.sample_size

    def add_inputs(self) -> None:
        super().add_inputs()
        min_val, max_val = st.slider(
            "Min Max values",
            min_value=-300.0,
            max_value=300.0,
            value=(0.0, 100.0),
            step=1.0,
            key="min_max"
        )

        if min_val == max_val:
            raise Exception("Min value and max value cannot be equal.")

