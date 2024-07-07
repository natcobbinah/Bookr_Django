import csv


def write_csv(filename, header, data):
    """
    :param str filename: The name of the file to which the data should be written
    :param list header: The header for the columns in csv file
    :param list data: The list of dicts mapping the values to the columns
    """
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print(f"Unable to write the contents to csv file {csv_file_error}")


if __name__ == '__main__':
    header = ['name', 'age', 'gender']
    data = [
        {'name': 'Richard', 'age': 32, 'gender': 'M'},
        {'name': 'Mumzil', 'age': 21, 'gender': 'F'},
        {'name': 'Melinda', 'age': 25, 'gender': 'F'},
    ]
    filename = 'sample_output_dict.csv'
    write_csv(filename, header, data)
