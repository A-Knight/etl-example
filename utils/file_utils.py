import os
import pandas as pd


def save_dataframe_to_csv(
    df: pd.DataFrame, output_dir: str, filename: str
) -> None:
    """
    Save a pandas DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_dir (str): The directory to save the file to.
        filename (str): The name of the file to save.
    """
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, filename), index=False)
    print(f"Data saved to {os.path.join(output_dir, filename)}")
