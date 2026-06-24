def write_summary(worksheet, summary, start_row=2):

    row = start_row

    for category, hours in summary.items():

        worksheet.cell(
            row=row,
            column=1,
            value=category,
        )

        worksheet.cell(
            row=row,
            column=2,
            value=hours,
        )

        row += 1


def write_matrix(
    worksheet,
    matrix,
    columns=None,
    row_header="Row",
    start_row=2,
):
    if not matrix:
        return

    if columns is None:

        discovered_columns = set()

        for values in matrix.values():
            discovered_columns.update(values.keys())

        columns = sorted(discovered_columns)

    worksheet.cell(
        row=start_row,
        column=1,
        value=row_header,
    )

    for col_idx, column in enumerate(columns, start=2):

        worksheet.cell(
            row=start_row,
            column=col_idx,
            value=column,
        )

    current_row = start_row + 1

    for row_name in sorted(matrix.keys()):

        worksheet.cell(
            row=current_row,
            column=1,
            value=row_name,
        )

        for col_idx, column in enumerate(columns, start=2):

            worksheet.cell(
                row=current_row,
                column=col_idx,
                value=matrix[row_name].get(column, 0),
            )

        current_row += 1

def write_table(
    worksheet,
    rows,
    start_row=2,
):
    if not rows:
        return

    headers = list(rows[0].keys())

    # Header Row

    for col_idx, header in enumerate(headers, start=1):

        worksheet.cell(
            row=start_row,
            column=col_idx,
            value=header,
        )

    # Data Rows

    current_row = start_row + 1

    for row_data in rows:

        for col_idx, header in enumerate(headers, start=1):

            worksheet.cell(
                row=current_row,
                column=col_idx,
                value=row_data.get(header),
            )

        current_row += 1