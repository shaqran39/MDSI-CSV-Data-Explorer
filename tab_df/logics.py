import pandas as pd


class Dataset:
    """
    --------------------
    Description
    --------------------
    -> Dataset (class): Class that manages a dataset loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (mandatory)
    -> df (pd.Dataframe): Pandas dataframe (default set to None)
    -> cols_list (list): List of columns names of dataset (default set to empty list)
    -> n_rows (int): Number of rows of dataset (default set to 0)
    -> n_cols (int): Number of columns of dataset (default set to 0)
    -> n_duplicates (int): Number of duplicated rows of dataset (default set to 0)
    -> n_missing (int): Number of missing values of dataset (default set to 0)
    -> n_num_cols (int): Number of columns that are numeric type (default set to 0)
    -> n_text_cols (int): Number of columns that are text type (default set to 0)
    -> table (pd.Series): Pandas DataFrame containing the list of columns, their data types and memory usage from dataframe (default set to None)
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.cols_list = []
        self.n_rows = 0
        self.n_cols = 0
        self.n_duplicates = 0
        self.n_missing = 0
        self.n_num_cols = 0
        self.n_text_cols = 0
        self.table = None

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.df to be displayed in the Dataframe tab of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        self.set_df()
        self.set_columns()
        self.set_dimensions()
        self.set_duplicates()
        self.set_missing()
        self.set_numeric()
        self.set_text()
        self.set_table()
        
        
    def set_df(self):
        """
        --------------------
        Description
        --------------------
        -> set_df (method): Class method that will load the uploaded CSV file as Pandas DataFrame and store it as attribute (self.df) if it hasn't been provided before.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_df_none():
            self.df = pd.read_csv(self.file_path)

    def is_df_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_df_none (method): Class method that checks if self.df is empty or none 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): Flag stating if self.df is empty or not

        """
        return self.df is None or self.df.empty
        

    def set_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_columns (method): Class method that extract the list of columns names and store the results in the relevant attribute (self.cols_list) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
            self.cols_list = self.df.columns.tolist()


    def set_dimensions(self):
        """
        --------------------
        Description
        --------------------
        -> set_dimensions (method): Class method that computes the dimensions (number of columns and rows) of self.df  and store the results in the relevant attributes (self.n_rows, self.n_cols) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
            self.n_rows, self.n_cols = self.df.shape

    def set_duplicates(self):
        """
        --------------------
        Description
        --------------------
        -> set_duplicates (method): Class method that computes the number of duplicated of self.df and store the results in the relevant attribute (self.n_duplicates) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
       
            duplicated_rows = self.df[self.df.duplicated(keep='first')]
            
            self.n_duplicates = len(duplicated_rows)

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing values of self.df and store the results in the relevant attribute (self.n_missing) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
            missing_values = self.df.isnull().values
            self.n_missing = missing_values.sum()


    def set_numeric(self):
        """
        --------------------
        Description
        --------------------
        -> set_numeric (method): Class method that computes the number of columns that are numeric type and store the results in the relevant attribute (self.n_num_cols) if self.df is not empty nor None 
        
        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
            cols = self.df.select_dtypes(include=['number']).columns
            self.n_num_cols = len(cols)


    def set_text(self):
        """
        --------------------
        Description
        --------------------
        -> set_text (method): Class method that computes the number of columns that are text type and store the results in the relevant attribute (self.n_text_cols) if self.df is not empty nor None 
        
        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
            cols = self.df.select_dtypes(include=['object']).columns
            self.n_num_cols = len(cols)

    def get_head(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_head (method): Class method that computes the first rows of self.df according to the provided number of rows specified as parameter (default: 5) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> n (int): Number of rows to be returned

        --------------------
        Returns
        --------------------
        -> (Pandas.DataFrame): First rows of dataframe

        """
        if not self.is_df_none():
            return self.df.head(n)

    def get_tail(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_tail (method): Class method that computes the last rows of self.df according to the provided number of rows specified as parameter (default: 5) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> n (int): Number of rows to be returned

        --------------------
        Returns
        --------------------
        -> (Pandas.DataFrame): Last rows of dataframe

        """
        if not self.is_df_none():
            return self.df.tail(n)

    def get_sample(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_sample (method): Class method that computes a random sample of rows of self.df according to the provided number of rows specified as parameter (default: 5) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> n (int): Number of rows to be returned

        --------------------
        Returns
        --------------------
        -> (Pandas.DataFrame): Sampled dataframe

        """
        if not self.is_df_none():
            return self.df.sample(n)


    def set_table(self):
        """
        --------------------
        Description
        --------------------
        -> set_table (method): Class method that computes the Dataframe containing the list of columns with their data types and memory usage and store the results in the relevant attribute (self.table) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
            # Create a DataFrame containing column names, data types, and memory usage
            column_info = self.df.dtypes.reset_index()
            column_info.columns = ["Column Name", "Data Type"]
            column_info["Memory Usage"] = self.df.memory_usage(deep=True) / 1024  # Convert to KB
            self.table = column_info

    def get_summary(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.df to be displayed in the Dataframe tab of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted dataframe to be displayed on the Streamlit app

        """
        if not self.is_df_none():
            # Create a summary DataFrame with description and value columns
            df = pd.DataFrame({
                "Description": ["Number of Rows", "Number of Columns", "Number of Duplicates", "Number of Missing Values", "Number of Numeric Columns", "Number of Text Columns"],
                "Value": [self.n_rows, self.n_cols, self.n_duplicates, self.n_missing, self.n_num_cols, self.n_text_cols]
            })
            return df