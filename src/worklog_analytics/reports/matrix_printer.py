def print_matrix(title: str, matrix: dict, columns: list[str] | None = None, row_header: str = "Row"):
    print(f"\n=========== {title} ===========\n")

    if columns is None:
        discovered_columns = set()

        for values in matrix.values():
            discovered_columns.update(values.keys())

        columns = sorted(discovered_columns)

    print(row_header.ljust(30)+ "".join(c.ljust(20) for c in columns))

    for row in sorted(matrix.keys()):
        line = row.ljust(30)

        for column in columns:
            hours = matrix[row].get(column, 0)
            line += (f"{hours:.1f}").ljust(20)

        print(line)
