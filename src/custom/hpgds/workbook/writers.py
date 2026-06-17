def write_summary(worksheet, summary, start_row=2):
    row = start_row

    for category, hours in summary.items():
        worksheet.cell(row=row, column=1, value=category)
        worksheet.cell(row=row, column=2, value=hours)
        row += 1

def write_matrix(worksheet, matrix, start_row=2):
    if not matrix:
        return

    headers = list(matrix[0].keys())

    for col, header in enumerate(headers, start=1):
        worksheet.cell(row=start_row, column=col, value=header)

    for row_idx, row_data in enumerate(matrix, start=start_row + 1):
        for col_idx, header in enumerate(headers, start=1):
            worksheet.cell(row=row_idx, column=col_idx, value=row_data[header])