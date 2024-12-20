import streamlit as st
import pandas as pd
import math
from pathlib import Path
from funcs import payload_only, bus_only
#========================================================================================================

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='MAPPER',
    page_icon='🛰️',
)

#========================================================================================================

st.title("MAPPER – Mass And Power Parameters Estimation Resource 🛰️")
st.markdown("""
Welcome to **MAPPER**, your go-to tool for automating spacecraft and payload budgeting! 🛰️

This app allows you to:
- Extract and analyze system parameters like **cost**, **mass**, and **power**.
- Streamline your budgeting and planning processes with ease.

### Let's make your next mission a success!
""")

#========================================================================================================

st.subheader("Preliminary Questions")

# Define the options for the dropdown
engineering_options = [" ", "Payload only", "Spacecraft Bus only","Both"]

# Create the dropdown
selected_engineering_option = st.selectbox("What unit is Pixxel engineering?", engineering_options, index=0)

#========================================================================================================
if selected_engineering_option == engineering_options[1]:
    st.write(f"{payload_only(selected_engineering_option)}")
if selected_engineering_option == engineering_options[2]:
    st.write(f"{bus_only(selected_engineering_option)}")
uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "xlsx", "json"])


