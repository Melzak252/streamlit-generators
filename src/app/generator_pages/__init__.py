import base64
from abc import ABC, abstractmethod

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


class GeneratorPage(ABC):
    @abstractmethod
    def get_values(self) -> np.ndarray:
        pass

    @abstractmethod
    def get_expected_value(self, x, *args, **kwargs) -> float:
        pass

    @abstractmethod
    def add_inputs(self) -> None:
        st.slider(
            "Bin size",
            min_value=1,
            max_value=10,
            value=5,
            key="bin_size"
        )

        st.number_input(
            "Sample Size",
            min_value=10,
            max_value=10_000_000,
            value=1000,
            step=10,
            key="sample_size"
        )

    def generate(self) -> None:
        st.session_state.generated_values = self.get_values()

    # Define a function to create a CSV file from a DataFrame
    def create_download_link(self, df, filename):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download CSV</a>'

    def add_diagrams(self) -> None:

        if "generated_values" not in st.session_state:
            st.session_state.generated_values = np.empty(st.session_state.sample_size)

        c1, c2 = st.columns([3, 1])
        # Create Altair chart

        x_values = np.linspace(
            np.min(st.session_state.generated_values),
            np.max(st.session_state.generated_values),
            100
        )

        y_values: np.linspace = self.get_expected_value(x_values)

        df: pd.DataFrame = pd.DataFrame({'x': x_values, 'y': y_values})

        try:
            hist: alt.Chart = alt.Chart(
                pd.DataFrame(st.session_state.generated_values, columns=["values"])).mark_bar().encode(
                x=alt.X("values:Q", bin=alt.Bin(step=st.session_state.bin_size), axis=alt.Axis(title="Value")),
                y=alt.Y("count()", axis=alt.Axis(title="Count"))
            )

            expected = alt.Chart(df).mark_line(color="red").encode(
                x="x",
                y="y"
            )

            chart = alt.layer(hist, expected).properties(title="Generated and expected values", height=400)
            c1.altair_chart(chart, use_container_width=True)

            # Add a button to download the DataFrame as a CSV file
            if c2.button('Download expected', use_container_width=True):
                self.create_download_link(df, 'expected_plot')

        except Exception as e:
            print(e)
