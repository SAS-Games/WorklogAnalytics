from worklog_analytics.reports.models import (SummaryReport, MatrixReport, TableReport)
from worklog_analytics.reports.excel_writers import (write_summary, write_matrix, write_table)


def write_report(worksheet, report):
    if isinstance(report, SummaryReport):
        write_summary(worksheet, report.data,)
    elif isinstance(report, MatrixReport):
        write_matrix(worksheet, report.data, report.columns, report.row_header)
    elif isinstance(report, TableReport):
        write_table(worksheet, report.rows,)
