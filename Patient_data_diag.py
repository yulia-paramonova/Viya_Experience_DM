import pandas as pd

input_df=SAS.sd2df(_input1)


# Assuming df is your input DataFrame
def classify_diagnosis(df):
    """
    Classifies primary diagnosis based on ICD-9 codes and creates a readmission indicator.
    Ensures data type compatibility between int and str variables.

    Parameters:
        df (pd.DataFrame): Input DataFrame with columns 'diag_1' and 'readmitted'.

    Returns:
        pd.DataFrame: DataFrame with new columns 'primary_diagnosis' and 'readmis'.
    """
    def get_primary_diagnosis(diag_1):
        """
        Safely classifies the diagnosis code, ensuring it is treated as integer.
        Returns a diagnosis category as string.
        """
        try:
            # Convert diag_1 to integer if possible
            code = int(diag_1)
        except (ValueError, TypeError):
            # If conversion fails, default to 'Other'
            return "Other"

        # Apply classification logic
        if code < 140:
            return "Other"
        elif 139 < code < 240:
            return "Neoplasms"
        elif 249 < code < 251:
            return "Diabetes"
        elif code < 460 or code == 785:
            return "Circulatory"
        elif code < 520 or code == 786:
            return "Respiratory"
        elif code < 580 or code == 787:
            return "Digestive"
        elif code < 630 or code == 788:
            return "Genitourinary"
        elif 710 <= code < 740:
            return "Musculoskeletal"
        elif 800 <= code <= 999:
            return "Injury"
        else:
            return "Other"

    # Safely apply diagnosis classification
    df['primary_diagnosis'] = df['diag_1'].apply(get_primary_diagnosis)

    def map_readmitted(x):
        """
        Converts 'readmitted' column to integer indicator.
        Returns 0 for 'NO', 1 otherwise. Handles missing values gracefully.
        """
        # Ensure x is treated as string for comparison
        if pd.isna(x):
            return 1  # Treat missing as readmitted
        return 0 if str(x).upper() == "NO" else 1

    # Safely apply readmission mapping
    df['Readmitted_flag'] = df['readmitted'].apply(map_readmitted)

    return df


# Example usage
# Assuming your input DataFrame is named input_df
output_df = classify_diagnosis(input_df)

SAS.df2sd(output_df,_output1)
