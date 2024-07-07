import xlsxwriter


def create_workbook(filename):
    """
    Create a new workbook on which we can work
    """
    workbook = xlsxwriter.Workbook(filename)
    return workbook


def create_worksheet(workbook):
    """
    Add a new worksheet in the workbook
    """
    worksheet = workbook.add_worksheet()
    return worksheet


def write_data(worksheet, data):
    """
    Write data to the worksheet
    """
    for row in range(len(data)):
        for col in range(len(data[row])):
            worksheet.write(row, col, data[row][col])

    # calculate average age
    worksheet.write(len(data), 0, "Avg. Age")
    # len(data) will give the next index to write to
    avg_formula = "=AVERAGE(B{}:B{})".format(1, len(data))
    worksheet.write(len(data), 1, avg_formula)


def close_workbook(workbook):
    """close an opened workbook"""
    workbook.close()


if __name__ == '__main__':
    data = [
        ['John Doe', 38],
        ['Adam Cuvver',  22],
        ['Stacy Martin',  28],
        ['Tom Harris',  42],
        ['Yuval Noah',  52],
    ]
    workbook = create_workbook('sample-workbook.xlsx')
    worksheet = create_worksheet(workbook)
    write_data(worksheet, data)
    close_workbook(workbook)
