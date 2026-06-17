from openpyxl import load_workbook

from custom.hpgds.calculators.employee_forecast_builder import build_employee_forecast
from custom.hpgds.reports.executive_summary import build_executive_summary
from custom.hpgds.reports.studio_support_breakdown import build_studio_support_breakdown
from custom.hpgds.reports.validation_summary import build_validation_summary
from custom.hpgds.reports.hpgds_forecast import build_hpgds_forecast
from custom.hpgds.reports.final_summary import build_final_summary
from custom.hpgds.reports.forecast_studio_breakdown import build_forecast_studio_breakdown
from custom.hpgds.reports.final_studio_breakdown import build_final_studio_breakdown
from custom.hpgds.workbook.report_registry import build_report_registry


def generate_workbook(
    worklogs,
    validation_issues,
    studio_groups_config,
    template_file,
    output_file,
    forecast_request = None,
):
    workbook = load_workbook(template_file)

    # Build Base Reports
    actual_summary = build_executive_summary(worklogs,studio_groups_config)
    studio_breakdown = build_studio_support_breakdown(worklogs, studio_groups_config)
    validation_summary = build_validation_summary (validation_issues)

    # Forecast Reports
    if forecast_request is not None:
        employee_forecast = build_employee_forecast(worklogs, forecast_request)
        forecast_summary = build_hpgds_forecast(worklogs, studio_groups_config, employee_forecast)
        final_summary = build_final_summary(actual_summary, forecast_summary)
        forecast_breakdown = build_forecast_studio_breakdown(employee_forecast, studio_breakdown)
        final_breakdown = build_final_studio_breakdown(studio_breakdown, forecast_breakdown)

    else:
        final_summary = actual_summary
        final_breakdown = studio_breakdown

    # Register Reports
    reports = build_report_registry(
        final_summary=final_summary,
        final_breakdown=final_breakdown,
        validation_summary=validation_summary,
    )

    # Write Reports
    for report in reports:

        worksheet = workbook[report.sheet_name]
        report.writer(worksheet, report.data)

    workbook.save(output_file)