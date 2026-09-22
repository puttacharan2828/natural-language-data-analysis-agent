import streamlit as st
import pandas as pd

from config import APP_NAME, APP_ICON, PAGE_LAYOUT

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout=PAGE_LAYOUT
)

st.title("📊 Natural Language Data Analysis Agent")

st.write(
    "Upload your dataset and ask questions about your data "
    "using natural language."
)

st.header("1. Upload Your Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")

    st.dataframe(df)

    st.header("2. Ask a Question")

question = st.text_input(
    "What would you like to know about the data?"
)

analyze_button = st.button("Analyze")

if analyze_button:

    if question:
        st.success("Question submitted successfully!")
        st.write("Your question:", question)

    else:
        st.warning("Please enter a question first.")