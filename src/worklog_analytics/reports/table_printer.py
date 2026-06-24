def print_table(title: str, rows: list[dict]):

    print()
    print(f"=========== {title} ===========")
    print()

    if not rows:
        print("(no data)")
        return

    headers = list(rows[0].keys())

    # Calculate column widths
    widths = {}

    for header in headers:
        widths[header] = len(header)

    for row in rows:
        for header in headers:
            widths[header] = max(
                widths[header],
                len(str(row.get(header, ""))),
            )

    # Header row

    header_line = ""

    for header in headers:
        header_line += header.ljust(widths[header] + 2)

    print(header_line)

    # Data rows

    for row in rows:

        line = ""

        for header in headers:
            line += str(
                row.get(header, "")
            ).ljust(widths[header] + 2)

        print(line)