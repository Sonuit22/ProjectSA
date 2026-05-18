import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("ProjectSA Dashboard")

# Sidebar
option = st.sidebar.selectbox("Choose a dataset", ["Random Data", "Custom Upload"])

if option == "Random Data":
    data = pd.DataFrame(np.random.randn(100, 3), columns=["A", "B", "C"])
else:
    uploaded_file = st.sidebar.file_uploader("Upload a CSV", type="csv")
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
    else:
        st.warning("Please upload a CSV file.")
        st.stop()

st.write("### Data Preview")
st.dataframe(data.head())

st.write("### Chart")
fig, ax = plt.subplots()
data.plot(kind="line", ax=ax)
st.pyplot(fig)
