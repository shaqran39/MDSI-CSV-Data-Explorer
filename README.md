# CSV Data Explorer Web Application - AT2 - 94692 Data Science Practice

## Authors
Group 22: 
- Md Tanzim Hossain (24692790)
- Ezilaan Irraivan (24695379)
- Jaime Garcia Y Garcia (13863992)
- Shaqran Saleh (25010238)

## Description
<What your application does>
This web application does preliminary exploration on a CSV file by allowing the users to explore the data in the file.
The application contains a menu for uploding a CSV file and a container containing 4 tabs displaying the information.
    1. The first tab provides overall information of the dataset and interactive exploration of the content.
    2. The second tab provides information on a numeric column as the user selects a numeric column and the tab provides analysed results.
    3. The third tab provides information on a text column as the user selects a text column and the tab provides analysed results.
    4. The fourth tab provides information on a datetime column as the user selects a datetime column and the tab provides analysed results.

<Some of the challenges you faced>
1. Setting up the self methods within the set_data methods
2. Retrieving the information of the particular series to be shown in the Altair charts
3. Setting up the session state in each respective tab
4. Pulling and pushing files to and fro from GitHub

<Some of the features you hope to implement in the future>
    1. Advanced Filtering Options
    2. Custom Visualizations
    3. High-level Comparisons
    4. Data Cleaning Features
    5. Machine Learning Integration
    6. Exporting Results

## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
1. Launch VS Code (version 1.83.0 [user setup], OS: Windows_NT x64 10.0.19045).
2. Open the folder containing all the python files.
3. Go to Manage, and select Command Palette (alternatively press Ctrl + Shift + P).
4. Search 'Python: Create Environment'
5. Click 'Venv', which creates a .venv (virtual environment in the workspace)
4. Select 'Select Interpreter'.
5. Choose the recommended Python interpreter (this project was developed with Python 3.9.11).

<Which Python version you used>
1. Python version: 3.9.11

<Which packages and version you used>
1. pip version: 22.0.4
2. json
    2.1 jsonschema version: 4.19.1
    2.2 jsonschema-specifications version: 2023.7.1
3. altair version: 5.1.2
4. streamlit version: 1.27.2

## How to Run the Program
<Provide instructions and examples>
1. Open the terminal, type "streamlit run streamlit_app.py" and it will automatically open with local host.
    1.1 The file directory must ensure that it is in the right folder or else the file will fail to launch.
    1.2 If the browser window does not automatically open, you can press control and click the link
        which will open a window in your browser.
    1.3 You can alternatively type http://localhost:8501 to go to the window.
2. Pressing control and c (Ctrl + C) in the terminal will stop the program from running, however active changes will be updated in real time
if the page is refreshed after the files are saved.

## Project Structure
<List all folders and files of this project and provide quick description for each of them>
Folders:
    1. app (holds the files for the main file to be run to run the web app)
    2. tab_date (holds the files for the datetime exploration part of the web app)
    3. tab_df (holds the files for the dataframe exploration part of the web app)
    4. tab_num (holds the files for the numeric exploration part of the web app)
    5. tab_text (holds the files for the text exploration part of the web app)

Files
    1. app (init and streamlit_app file meant to run the whole app)
    2. tab_date (init, display and logics file with display meant for the design of the tab and the logics for the computations)
    3. tab_df (init, display and logics file with display meant for the design of the tab and the logics for the computations)
    4. tab_num (init, display and logics file with display meant for the design of the tab and the logics for the computations)
    5. tab_text (init, display and logics file with display meant for the design of the tab and the logics for the computations)
    6. README.md (containing information about the team and project description)

## Citations
<Mention authors and provide links code you source externally>
1. https://www.geeksforgeeks.org/python-programming-language/
2. https://www.youtube.com/watch?v=eL_0Ok_Gkas
3. https://docs.streamlit.io/
