
import streamlit as st

from app.generator_pages.page_map import MAP_PAGES

if __name__ == '__main__':
    selected = st.selectbox(
        "Select generator",
        MAP_PAGES.keys()
    )
    page = MAP_PAGES[selected]()

    try:
        page.add_inputs()

        if st.button("REGENERATE", use_container_width=True):
            page.generate()

        page.add_diagrams()
    except Exception as e:
        st.error(e)