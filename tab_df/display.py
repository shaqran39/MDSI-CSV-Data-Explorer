import streamlit as st

from logics import Dataset

def display_tab_df_content(file_path):
    """
    --------------------
    Description
    --------------------
    -> display_overall_df (function): Function that will instantiate tab_df.logics.Dataset class, save it into Streamlit session state and call its tab_df.logics.Dataset.set_data() method in order to compute all information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    1. the results of tab_df.logics.Dataset.get_summary() as a Streamlit Table
    2. the results of tab_df.logics.Dataset.table using Streamlit.write()
    Finally it will display a second Streamlit Expander container with a slider to select the number of rows to be displayed and a radio button to select the method (head, tail, sample).
    According to the values selected on the slider and radio button, display the subset of the dataframe accordingly using Streamlit.dataframe
    
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file

    --------------------
    Returns
    --------------------
    -> None
    
    """
   
    dataset = Dataset(file_path)
    dataset.set_data()

    # summary
    with st.expander("Dataset Summary"):
        summary = dataset.get_summary()
        st.table(summary)

    # column info
    with st.expander("Column Information"):
        if dataset.table is not None:
            st.write(dataset.table)

    # displaying dataset
    with st.expander("Display Subset"):
        # Slider to select the number of rows to display
        num_rows = st.slider("Select the number of rows to display", min_value=1, max_value=dataset.n_rows, value=5)

        # Radio button to select the method (head, tail, sample)
        method = st.radio("Select the method", ("Head", "Tail", "Sample"))

        # Display the selected subset of the dataset
        if method == "Head":
            st.dataframe(dataset.get_head(num_rows))
        elif method == "Tail":
            st.dataframe(dataset.get_tail(num_rows))
        elif method == "Sample":
            st.dataframe(dataset.get_sample(num_rows))

# Streamlit app code
st.title("CSV Exploration")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    # Call the display_tab_df_content function to display dataset information
    display_tab_df_content(uploaded_file)
