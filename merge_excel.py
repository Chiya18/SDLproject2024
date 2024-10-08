import pandas as pd

def merge_excel(file1, file2):
    # Read the Excel files with the correct header row (9th row = index 8)
    df1 = pd.read_excel(file1, header=9)
    df2 = pd.read_excel(file2, header=9)

    # Check if "Enrollment Number" exists in both files
    if 'Enrollment Number' not in df1.columns or 'Enrollment Number' not in df2.columns:
        raise ValueError("Missing 'Enrollment Number' column in one of the Excel files")

    # Merge the dataframes on the 'Enrollment Number' column
    merged_df = pd.merge(df1, df2, on='Enrollment Number')

    # Calculate the total attendance for each student (adjust columns as per your actual data)
    if 'Mid Term Test Attendance' in merged_df.columns and 'Quiz Attendance' in merged_df.columns:
        merged_df['Total Attendance'] = merged_df['Mid Term Test Attendance'] + merged_df['Quiz Attendance']
    else:
        raise ValueError("Missing required attendance columns in the merged data")

    # Return the merged dataframe
    return merged_df
