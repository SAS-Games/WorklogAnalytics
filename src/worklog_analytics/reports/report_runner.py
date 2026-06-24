from worklog_analytics.models.analysis_context import AnalysisContext
from worklog_analytics.reports.report_filter import filter_worklogs
from worklog_analytics.reports.report_builder import build_summary
from worklog_analytics.reports.matrix_builder import build_matrix
from worklog_analytics.reports.models import (SummaryReport, MatrixReport)


def _build_summary_report(
    context,
    filtered_worklogs,
    report_config,
):

    expected_values = None

    if report_config["group_by"] == "activity_group":
        expected_values = [
            group["name"] for group in context.activity_config["activity_groups"]
        ]

    summary = build_summary(
        filtered_worklogs,
        report_config["group_by"],
        include_none=not report_config.get(
            "exclude_none",
            False,
        ),
        expected_values=expected_values,
    )

    return SummaryReport(
        title=report_config["title"],
        worksheet_name=report_config.get("worksheet_name"),
        data=summary,
    )


def _build_matrix_report(
    context,
    filtered_worklogs,
    report_config,
):

    expected_columns = None

    if report_config["columns"] == "activity_group":

        expected_columns = [
            group["name"] for group in context.activity_config["activity_groups"]
        ]

    matrix, columns = build_matrix(
        filtered_worklogs,
        report_config["rows"],
        report_config["columns"],
        expected_columns,
    )

    return MatrixReport(
        title=report_config["title"],
        worksheet_name=report_config.get("worksheet_name"),
        data=matrix,
        columns=columns,
        row_header=report_config.get(
            "row_header",
            "Row",
        ),
    )


def run_reports(context: AnalysisContext):

    reports = []

    worklogs = context.worklogs
    reports_config = context.reports_config

    for report in reports_config["reports"]:

        filtered_worklogs = worklogs

        if "filters" in report:
            filtered_worklogs = filter_worklogs(
                worklogs,
                report["filters"],
            )

        if report.get("type") == "matrix":

            reports.append(
                _build_matrix_report(
                    context,
                    filtered_worklogs,
                    report,
                )
            )

        else:

            reports.append(
                _build_summary_report(
                    context,
                    filtered_worklogs,
                    report,
                )
            )

    return reports
