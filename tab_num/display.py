import streamlit as st

from tab_num.logics import NumericColumn

def display_tab_num_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_num_content (function): Function that will instantiate tab_num.logics.NumericColumn class, 
    save it into Streamlit session state and call its tab_num.logics.NumericColumn.find_num_cols() method in order to find all numeric columns.
    
    Then it will display a Streamlit select box with the list of numeric columns found.
    
    Once the user select a numeric column from the select box, it will call the tab_num.logics.NumericColumn.set_data() method in order to compute all the information to be displayed.
    
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_num.logics.NumericColumn.get_summary() as a Streamlit Table
    - the graph from tab_num.logics.NumericColumn.histogram using Streamlit.altair_chart()
    - the results of tab_num.logics.NumericColumn.frequent using Streamlit.write
 
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file (optional)
    -> df (pd.DataFrame): Loaded dataframe (optional)

    --------------------
    Returns
    --------------------
    -> None

    """
    numeric = NumericColumn(file_path)
    if "mdf" not in st.session_state:
        st.session_state.mdf = numeric

    cols = numeric.find_num_cols()
    
    option = st.selectbox('Which Numeric Column do you want to explore?', cols)

    numeric.set_data(option)

     # Summary of Numeric Columns exploration
    with st.expander("Dataset Summary"):
        summary = numeric.get_summary()
        st.table(summary)

    # Plot bar chat and display in Web App
    st.markdown('**Histogram**')
    st.altair_chart(numeric.set_histogram())

    # Create a frequent table and display in WebApp
    st.markdown('**Most Frequent Values**')
    frequent = numeric.set_frequent()
    st.write(frequent)