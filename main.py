from app.io.input import *
from app.io.output import *


def main():
    data = [
        ("Name", "Age", "City"),
        ("John", 30, "New York"),
        ("Alice", 25, "Los Angeles"),
        ("Bob", 35, "Chicago")
    ]
    write_to_file("data/data.txt", input_from_console())
    write_to_csv("data/data_csv.csv", data)
    output_to_console(read_from_file("data/data.txt"))
    print(read_from_file_using_pandas("data/data_csv.csv"))


if __name__ == '__main__':
    main()


