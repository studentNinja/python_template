import pandas as pd


def output_to_console(text):
    """
    Function to output text to console.

    Args:
        text (str): The text to be printed in console.
    """
    print(text)


def read_from_file(file_path):
    """
    Function to read from a file using Python's default read() function.

    Args:
    -----
        file_path (str): The path to the file to be read.

    Returns:
    --------
        str: Content read from the file.
            Returns None if file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def read_from_file_using_pandas(file_path):
    """
    Function to read from a file using pandas.

    Args:
    -----
        file_path (str): Path to file .

    Returns:
    --------
        pandas.DataFrame: Data read from the file using Pandas.
            Returns None if file is not found.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


if __name__ == "__main__":
    pass
