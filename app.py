import streamlit as st
from utils import cube, fifth_power, square

# Set page configuration
st.set_page_config(page_title="Power Calculator", page_icon="🔢")

# Streamlit UI Header
st.title("🔢 Power Calculator")
st.markdown("""
Welcome to the Power Calculator!
Enter a number below to see its **square**, **cube**, and **fifth power**.
---
""")

# Get user input with validation
# We use step=1 to ensure integer inputs
n = st.number_input("Enter an integer:", value=1, step=1)

# Perform calculations using utility functions
sq_res = square(n)
cu_res = cube(n)
fi_res = fifth_power(n)

# Display results in columns for a better UI
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Square", value=sq_res)
    st.caption(f"{n}²")

with col2:
    st.metric(label="Cube", value=cu_res)
    st.caption(f"{n}³")

with col3:
    st.metric(label="Fifth Power", value=fi_res)
    st.caption(f"{n}⁵")

st.markdown("---")
st.info("This project demonstrates MLOps CI practices with Streamlit and GitHub Actions.")
