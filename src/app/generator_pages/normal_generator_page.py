import numpy as np
import streamlit as st

from app.generator_pages import GeneratorPage
from random_generators.normal import NormalGenerator


class NormalGeneratorPage(GeneratorPage):
    def get_expected_value(self, x, *args, **kwargs) -> float:
        return np.exp(-self._exponent(x) * self._exponent(x) / 2) * self._constant

    def _exponent(self, x) -> float:
        return (x - st.session_state.mean) / st.session_state.dev

    def get_values(self) -> np.ndarray:
        return NormalGenerator.generate(
            mean=st.session_state.mean,
            dev=st.session_state.dev,
            sample_size=st.session_state.sample_size
        )

    @property
    def _constant(self) -> float:
        return (st.session_state.bin_size * st.session_state.sample_size) / (st.session_state.dev * np.sqrt(2 * np.pi))

    def add_inputs(self) -> None:
        super().add_inputs()
        col1, col2 = st.columns(2)
        col1: st.delta_generator.DeltaGenerator
        col2: st.delta_generator.DeltaGenerator

        with col1:
            col1.number_input(
                "Standard deviation",
                min_value=0.0,
                max_value=100.0,
                value=15.0,
                step=0.5,
                key="dev"
            )

        with col2:
            col2.number_input(
                "Mean",
                min_value=-1000.0,
                max_value=1000.0,
                value=100.0,
                step=1.,
                key="mean"
            )