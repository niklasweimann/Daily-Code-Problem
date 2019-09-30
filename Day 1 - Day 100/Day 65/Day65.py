
def print_matrix_clockwise(matrix: [[]]):
    column_count = len(matrix[0])
    row_count = len(matrix)
    start_row_index = 0
    start_column_index = 0
    result_string = ""

    while start_row_index < row_count and start_column_index < column_count:
        for i in range(start_column_index, column_count):
            result_string += "{} ".format(matrix[start_row_index][i])

        start_row_index += 1

        for i in range(start_row_index, row_count):
            result_string += "{} ".format(matrix[i][column_count-1])

        column_count -= 1

        if start_row_index < row_count:
            for i in range(column_count - 1, start_column_index - 1, -1):
                result_string += "{} ".format(matrix[row_count - 1][i])
            row_count -= 1

        if start_column_index < column_count:
            for i in range(row_count - 1, start_row_index - 1, -1):
                result_string += "{} ".format(matrix[i][start_column_index])
            start_column_index += 1

    return result_string


matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

print(print_matrix_clockwise(matrix))
