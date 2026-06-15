from worklog_analytics.models.analysis_context import AnalysisContext
from worklog_analytics.reports.report_filter import filter_worklogs
from worklog_analytics.reports.report_builder import build_summary
from worklog_analytics.reports.report_printer import print_summary
from worklog_analytics.reports.matrix_builder import build_matrix
from worklog_analytics.reports.matrix_printer import print_matrix


def run_reports(context: AnalysisContext):

    worklogs = context.worklogs
    reports_config = context.reports_config

    for report in reports_config["reports"]:
        filtered_worklogs = worklogs

        if "filters" in report:
            filtered_worklogs = filter_worklogs(worklogs, report["filters"])

        # Matrix Report
        if report.get("type") == "matrix":
            expected_columns = None
            if report["columns"] == "activity_group":

                expected_columns = [
                    group["name"]
                    for group in context.activity_config["activity_groups"]
                ]

            matrix, columns = build_matrix(filtered_worklogs, report["rows"], report["columns"], expected_columns)
            print_matrix(report["title"], matrix, columns)
            continue

        # Summary Report
        expected_values = None

        if report["group_by"] == "activity_group":
            expected_values = [
                group["name"] for group in context.activity_config["activity_groups"]
            ]

        summary = build_summary(
            filtered_worklogs,
            report["group_by"],
            include_none=not report.get("exclude_none", False),
            expected_values=expected_values,
        )

        print_summary(report["title"], summary)
