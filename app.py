import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set page title
st.set_page_config(page_title="My FirstStreamlit App", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("What page should I open?", ["Overall", "Introduction", "Methodology", "Results", "Recommendations"])
