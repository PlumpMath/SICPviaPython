def f(row, column):
    if column == row or column == 1:
        return 1
    else:
        return f(row - 1, column - 1) + f(row - 1, column)
