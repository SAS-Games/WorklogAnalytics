from worklog_analytics.reports.models import (SummaryReport,MatrixReport,TableReport)
from worklog_analytics.reports.report_printer import print_summary
from worklog_analytics.reports.matrix_printer import print_matrix
from worklog_analytics.reports.table_printer import print_table
from worklog_analytics.reports.models import Report


def render_reports(reports: list[Report]):
    for report in reports:
        if not report.render_console:
            continue
        if isinstance(report, SummaryReport):
            print_summary(   report.title,report.data)
        elif isinstance(report, MatrixReport):
           print_matrix(report.title, report.data, report.columns, report.row_header)
        elif isinstance(report, TableReport):
            print_table(report.title, report.rows,)            