# 06/27/2019
# import numpy as np

# This is for "type hints". Totally optional and Python doesn't actually enforce
# that if you say a function takes in a List it actually does, but I find they're
# helpful for documentation purposes
# The base "primitive" types like str, int, float, bool don't need to be imported.
# List, Dict, Set, Tuple, etc. all need to be imported, however.
# https://docs.python.org/3/library/typing.html
from typing import List

# INPUT MATRIX DIMENSIONS
#print("matrix m x n. input dimensions:")

# checking for n x n dimensions
# dim_'x' = dimension in type 'x'
"""
dim_str = input("")
dim_list = dim_str.split(" ")
valid = False
"""

# I have no idea what I'm doing lines 14-29
"""
while not valid:
    try:
        dim_list[0]
        valid = True
    except IndexError:
        print("Invalid input. Reenter dimensions.")
        dim_str = input("")

while dim_list[0] != dim_list[2]:
    print("Invalid matrix. Accept only matrices of n x n.")
    dim_str = input("")
    dim_list = dim_str.split(" ")
else:
    pass
"""

# dim = int(dim_list[0])


# INPUT MATRIX VALUES
# mat_row = list of one row in matrix
# mat_val = list of 'mat_row'

# "Helper functions" are functions that are only used
# internally inside the files they're defined and not meant
# to be used or exposed by the user. When you want to define a
# helper function, it's good practice to pre-pend its name with
# double underscores (__) to help hide it from the user.
def __is_str_numeric(string: str) -> bool:
    """
    Helper function that checks whether string is integer or float.

    Parameters
    ----------
    string

    Returns
    -------
    bool
    """
    try:
        float(string)
    except ValueError:
        return False
    return True


def input_matrix() -> List[List[float]]:
    """
    Takes in user input and returns defined matrix.

    Returns
    -------
    List[List[float]]: user-defined matrix of floats
    """

    num_rows = input("Input the number of rows: ")
    # The "isdigit()" string method checks whether a
    # string is a positive integer. We then check
    # whether the input is equal to 0 as well.
    while not num_rows.isdigit() or not int(num_rows):
        num_rows = input("Invalid row input. Try again: ")
    num_rows = int(num_rows)

    num_cols = input("Input the number of cols: ")
    while not num_cols.isdigit() or not int(num_cols):
        num_cols = input("Invalid col input. Try again: ")
    num_cols = int(num_cols)

    matrix = []

    for row_num in range(1, num_rows+1):
        input_row = input(f"Row {row_num}: ")
        while True:  # Runs forever until broken out of
            # Check each entry is either an integer or a float
            # parsed_row then becomes a list of boolean (True/False) values
            parsed_row = [__is_str_numeric(entry) for entry in input_row.split(",")]
            # Check dimensions match
            if len(parsed_row) != num_cols:
                print(f"Expected {num_cols} entries. Got {len(parsed_row)}. Try again.")
                input_row = input(f"Row {row_num}: ")
            # parsed_row is now a list of booleans. The all() function checks
            # if an iterable is all True. In this case, it's really checking that
            # all entries in input_row are all either an int or a float
            # https://docs.python.org/3/library/functions.html#all
            elif not all(parsed_row):
                print(f"Please only enter integers or floats. Try again.")
                input_row = input(f"Row {row_num}: ")
            else:
                # Break out of the while-loop because the condition
                # is satisfied
                validated_row = [float(entry) for entry in input_row.split(",")]
                matrix.append(validated_row)
                break

    print("Generated matrix:")
    for row in matrix:
        print(row)

    return matrix


def row_input():
    row_number = 1

    print("Input matrix row by row\n"
          "Separate terms by commas\n"
          "Press enter after each row\n")
    mat_vals = ""
    for a in range(dim):
        mat_row = input(f"row {row_number}: ")
        compatible = False
        while not compatible:
            try:
                row = [float(num) for num in mat_row.split(",")]

                # checking for dimension fit
                if len(row) != dim:
                    print("M Format is not compatible. Re-enter row.")
                    mat_row = input(f"row {row_number}: ")
                # "elif" is a contraction for "else if"
                # It's handy for avoiding deep layers of indentation
                elif row_number != 1:
                    # applies only after first input
                    mat_vals += ','
                else:
                    pass
                row_number += 1
                mat_vals += mat_row
                compatible = True

            # checking for format fit
            except ValueError:
                print("Format is not compatible. Reenter row.")
                mat_row = input(f"row {row_number}: ")
    return mat_vals


"""
# CONVERTING SEPARATED ROW INPUTS TO ONE MATRIX
# num_'x' = entered numbers in type 'x'
num_str = row_input()
num_list = [float(num) for num in num_str.split(",")]
num_mat = [num_list[i * dim:(i + 1) * dim] for i in range((dim ** 2 + dim - 1) // dim)]
A = matrix_A = np.array(num_mat)
"""


def diag_mat(matrix):
    """
    ROW REDUCING (rrf) TO A DIAGONAL MATRIX
    a = row being reduced to zero
    b = row remaining in the diagonal
    c and d scale rows a and b to the same number

    Parameters
    ----------
    matrix

    Returns
    -------

    """
    for b in range(len(matrix)):
        for a in range(len(matrix[0])):
            if a <= b:
                pass

            # in Python, 0 is a "falsey" value (https://docs.python.org/2.4/lib/truth.html)
            # therefore, checking whether something is equivalent to zero is the same as
            # checking whether its "false". It's convention to use "not (variable)" instead
            # of "(variable) == 0"
            if not matrix[b][b]:
                # avoiding ZeroDivisionError
                pass

            # The "else" here is unnecessary because if the two conditions above pass
            # it will always run
            matrix[a] = matrix[a] - matrix[b] * (matrix[a][b] / matrix[b][b])
    # "\n" is special text formatting code meaning "new line"
    print(f"Diagonal matrix:\n{matrix}")


def multiply_diag(matrix):
    """
    FINDING THE DETERMINANT BY MULTIPLYING DIAGONAL
    l = number of values in the diagonal
    m = diagonal position (A[m][m] = diagonal value)
    n = multiplied diagonal values complied: determinant

    Parameters
    ----------
    matrix

    Returns
    -------

    """
    n = matrix[0][0]
    for l in range(len(matrix)-1):
        m = l + 1
        n *= float(matrix[m][m])
    # undoing negative zero answers
    if n == -0:
        n = abs(n)
    print(f"determinant of matrix: {n}")
    return n


# LINEAR INDEPENDENCE
def is_linearly_independent(matrix: List[List[float]]) -> bool:
    """
    Parameters
    ----------
    List[List[float]]: 2D matrix of floats

    Returns
    -------
    bool: Whether matrix is linearly independent
    """

    determinant = multiply_diag(matrix)
    if not determinant:
        print("Matrix is linearly dependent.")
        return False
    # Don't need to explicitly write "else" here
    print("Matrix is linearly independent.")
    return True


def main():
    matrix = input_matrix()
    # print(is_linearly_independent(matrix))
    # print(multiply_diag(matrix))


if __name__ == "__main__":
    # If you click the green arrow to the left of this
    # and select "run" from the dropdown it will run
    # the "main" function above

    # This tells the computer where to "enter" the program
    # if you ran "python3 determinant-calculator.py" through a terminal
    # it would enter this if statement and then execute the main() function.
    # It's a good idea to use the main statement to control the execution of your
    # program/code. Without it, the code will simply execute top to bottom
    # which can cause some headaches and errors. By splitting things up into
    # functions we can control the order and circumstance of execution.
    main()
