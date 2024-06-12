import pandas as pd
import altair as alt


class NumericColumn:
    """
    --------------------
    Description
    --------------------
    -> NumericColumn (class): Class that manages a column of numeric data type

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (optional)
    -> df (pd.Dataframe): Pandas dataframe (optional)
    -> cols_list (list): List of columns names of dataset that are numeric type (default set to empty list)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (default set to None)
    -> n_unique (int): Number of unique value of a serie (default set to None)
    -> n_missing (int): Number of missing values of a serie (default set to None)
    -> col_mean (int): Average value of a serie (default set to None)
    -> col_std (int): Standard deviation value of a serie (default set to None)
    -> col_min (int): Minimum value of a serie (default set to None)
    -> col_max (int): Maximum value of a serie (default set to None)
    -> col_median (int): Median value of a serie (default set to None)
    -> n_zeros (int): Number of times a serie has values equal to 0 (default set to None)
    -> n_negatives (int): Number of times a serie has negative values (default set to None)
    -> histogram (alt.Chart): Altair histogram displaying the count for each bin value of a serie (default set to empty)
    -> frequent (pd.DataFrame): Datframe containing the most frequest value of a serie (default set to empty)

    """
    def __init__(self, file_path=None, df=None):
        self.file_path = file_path
        self.df = df
        self.cols_list = []
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.col_mean = None
        self.col_std = None
        self.col_min = None
        self.col_max = None
        self.col_median = None
        self.n_zeros = None
        self.n_negatives = None
        self.histogram = alt.Chart()
        self.frequent = pd.DataFrame(columns=['value', 'occurrence', 'percentage'])

    def find_num_cols(self):
        """
        --------------------
        Description
        --------------------
        -> find_num_cols (method): Class method that will load the uploaded CSV file as Pandas DataFrame and store it as attribute (self.df) if it hasn't been provided before.
        Then it will find all columns of numeric data type and store the results in the relevant attribute (self.cols_list).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        
        self.df = pd.read_csv(self.file_path)
        self.cols_list = self.df._get_numeric_data().columns.values.tolist()
        return self.cols_list
        
        

    def set_data(self, col_name):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that sets the self.serie attribute with the relevant column from the dataframe and then computes all requested information from self.serie to be displayed in the Numeric section of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> col_name (str): Name of the numeric column to be analysed

        --------------------
        Returns
        --------------------
        -> None

        """
        x = self.df[col_name]
        self.serie = pd.Series(x)        
        self.set_unique()
        self.set_missing()
        self.set_zeros()
        self.set_negatives()
        self.set_mean()
        self.set_std()
        self.set_min()
        self.set_max()
        self.set_median()
        self.set_histogram()
        self.set_frequent()
        return col_name

    def convert_serie_to_num(self):
        """
        --------------------
        Description
        --------------------
        -> convert_serie_to_num (method): Class method that convert a Pandas Series to numeric data type and store the results in the relevant attribute (self.serie).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.serie = pd.to_numeric(self.df)
        return self.serie


    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): Flag stating if the serie is empty or not

        """
        if len(self.serie) == 0:
            return self.serie is None
        
        

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique values of a column and store the results in the relevant attribute (self.n_unique)

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_unique = len(self.serie.unique())
        return self.n_unique
        

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie and store the results in the relevant attribute (self.n_missing) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_missing = self.serie.isna().sum()
        return self.n_missing
        

    def set_zeros(self):
        """
        --------------------
        Description
        --------------------
        -> set_zeros (method): Class method that computes the number of times a serie has values equal to 0 and store the results in the relevant attribute (self.n_zeros) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_zeros = (self.serie == 0).sum()
        return self.n_zeros
        

    def set_negatives(self):
        """
        --------------------
        Description
        --------------------
        -> set_negatives (method): Class method that computes the number of times a serie has negative values and store the results in the relevant attribute (self.n_negatives) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.n_negatives = (self.serie < 0).sum()
        return self.n_negatives
        

    def set_mean(self):
        """
        --------------------
        Description
        --------------------
        -> set_mean (method): Class method that computes the average value of a serie and store the results in the relevant attribute (self.col_mean) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.col_mean = self.serie.mean()
        return self.col_mean
        

    def set_std(self):
        """
        --------------------
        Description
        --------------------
        -> set_std (method): Class method that computes the standard deviation value of a serie and store the results in the relevant attribute (self.col_std) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.col_std = self.serie.std()
        return self.col_std
        
    
    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie and store the results in the relevant attribute (self.col_min) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.col_min = self.serie.min()
        return self.col_min
        

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the maximum value of a serie and store the results in the relevant attribute (self.col_max) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.col_max = self.serie.max()
        return self.col_max
        

    def set_median(self):
        """
        --------------------
        Description
        --------------------
        -> set_median (method): Class method that computes the median value of a serie and store the results in the relevant attribute (self.col_median) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.col_median = self.serie.median()
        return self.col_median
        

    def set_histogram(self):
        """
        --------------------
        Description
        --------------------
        -> set_histogram (method): Class method that computes the Altair histogram displaying the count for each bin value of a serie and store the results in the relevant attribute (self.histogram)

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        self.histogram = alt.Chart(self.serie.reset_index()).mark_bar().encode(alt.X(f"{self.serie.name}", bin=True), y='count()',)
        return self.histogram


    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie and store the results in the relevant attribute (self.frequent)

        --------------------
        Parameters
        --------------------
        -> end (int):
            Parameter indicating the maximum number of values to be displayed

        --------------------
        Returns
        --------------------
        -> None

        """
        freq_info = {'value':self.serie}
        freq_df = pd.DataFrame(freq_info)
        freq_df = freq_df.head(end)
        self.frequent = self.frequent.assign(value=freq_df.head(end))
        self.frequent = freq_df.groupby('value').size().reset_index(name = 'occurrence')
        self.frequent['percentage'] = self.frequent['occurrence']/self.frequent['occurrence'].sum()
        return self.frequent
        
        
    def get_summary(self,):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): 
        Class method that formats all requested information from self.serie to be displayed 
        in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted dataframe to be displayed on the Streamlit app

        """
    
        summary = pd.DataFrame({
                "Description": ["Number of Unique Values", "Number of Missing Values", "Number of Rows with 0", "Number of Rows with Negative Values", "Average Value", "Standard Deviation Value", "Minimum Value", "Maximum Value", "Median Value"],
                "Value": [self.n_unique, self.n_missing, self.n_zeros, self.n_negatives, self.col_mean, self.col_std, self.col_min, self.col_max, self.col_median]
            })
        return summary