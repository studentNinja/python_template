import pandas as pd


def input_from_console():
    """
    Function to input text from console.

    Returns:
        str: Text entered from the console.
    """
    user_input = input("Enter text from the console: ")
    return user_input


def write_to_file(file_path, content):
    """
    Function to write content to a file using Python's write() function.

    Args:
        file_path (str): The path to the file.
        content (str): The content to be written to file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred while writing to {file_path}: {e}")


def write_to_csv(file_path, data):
    """
    Writes data to a CSV file.

    Args:
        file_path (str): The path to file.
        data : The data written to CSV file.

    Returns:
        bool: True if successful, else False.
    """
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        return True
    except Exception as e:
        print(f"An error occurred while writing to CSV file '{file_path}': {e}")
        return False


if __name__ == "__main__":
    pass
