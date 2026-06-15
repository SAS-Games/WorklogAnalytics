from collections import defaultdict


def build_matrix(worklogs, rows: str, columns: str, expected_columns: list[str] | None = None):

    matrix = defaultdict(lambda: defaultdict(float))

    for worklog in worklogs:
        row = getattr(worklog, rows, None) or f"No {rows}"
        column = getattr(worklog, columns, None) or f"No {columns}"
        matrix[row][column] += worklog.hours

    return matrix, expected_columns
