import streamlit as st

from config import APP_NAME, APP_ICON, PAGE_LAYOUT
from data.loader import load_dataset


st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout=PAGE_LAYOUT
)

st.title("📊 Intelligent Business Data Analysis Agent")

st.write(
    "Upload your dataset and ask questions about your data "
    "using natural language."
)

st.header("1. Upload Your Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    try:
        df = load_dataset(uploaded_file)

        st.success("Dataset uploaded successfully!")

        st.subheader("Dataset Preview")

        st.dataframe(df)

        st.subheader("Dataset Information")

        st.write("Number of Rows:", df.shape[0])
        st.write("Number of Columns:", df.shape[1])
        st.write("Column Names:", list(df.columns))
        
        st.write("Data Types:")
        st.write(df.dtypes)



    except ValueError as e:
        st.error(str(e))

    except Exception:
        st.error(
            "Something went wrong while loading the dataset. "
             "Please check that the file is valid and try again."
    )


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