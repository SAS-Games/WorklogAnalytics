from worklog_analytics.reports.models import SummaryReport
from custom.hpgds.reports.executive_summary import build_executive_summary
from custom.hpgds.reports.studio_support_breakdown import build_studio_support_breakdown
from custom.hpgds.reports.validation_summary import build_validation_summary
from custom.hpgds.reports.hpgds_forecast import build_hpgds_forecast
from custom.hpgds.reports.forecast_summary import build_forecast_summary
from custom.hpgds.reports.final_summary import build_final_summary
from custom.hpgds.reports.forecast_studio_breakdown import build_forecast_studio_breakdown
from custom.hpgds.reports.final_studio_breakdown import build_final_studio_breakdown
from custom.hpgds.calculators.employee_forecast_builder import build_employee_forecast


def build_hpgds_reports(
    worklogs,
    validation_issues,
    studio_groups_config,
    forecast_request=None,
):

    reports = []

    # Actual Summary

    actual_summary = build_executive_summary(
        worklogs,
        studio_groups_config,
    )

    reports.append(
        SummaryReport(
            title="HP-GDS EFFORT SUMMARY",
            worksheet_name="Effort Summary",
            data=actual_summary
        )
    )

    # Studio Breakdown

    studio_breakdown = build_studio_support_breakdown(
        worklogs,
        studio_groups_config,
    )

    reports.append(
        SummaryReport(
            title="STUDIO SUPPORT BREAKDOWN",
            worksheet_name="Studio Support Summary",
            data=studio_breakdown,
        )
    )

    # Forecast Reports

    if forecast_request is not None:

        employee_forecast = build_employee_forecast(
            worklogs,
            forecast_request,
        )

        forecast = build_hpgds_forecast(
            worklogs,
            studio_groups_config,
            employee_forecast,
        )

        forecast_summary = build_forecast_summary(
            actual_summary,
            forecast,
        )

        reports.append(
            SummaryReport(
                title="FORECASTED EFFORT SUMMARY",
                worksheet_name="Forecast Summary",
                data=forecast_summary,
                render_console=True,
                render_excel=False,
            )
        )

        final_summary = build_final_summary(
            actual_summary,
            forecast,
        )

        reports.append(
            SummaryReport(
                title="FINAL EFFORT SUMMARY",
                worksheet_name="Final Summary",
                data=final_summary,
            )
        )

        forecast_breakdown = build_forecast_studio_breakdown(
            employee_forecast,
            studio_breakdown,
        )

        reports.append(
            SummaryReport(
                title="FORECASTED STUDIO SUPPORT BREAKDOWN",
                worksheet_name="Forecast Studio Support",
                data=forecast_breakdown,
                render_excel=False,
            )
        )

        final_breakdown = build_final_studio_breakdown(
            studio_breakdown,
            forecast_breakdown,
        )

        reports.append(
            SummaryReport(
                title="FINAL STUDIO SUPPORT BREAKDOWN",
                worksheet_name="Final Studio Support Summary",
                data=final_breakdown,
            )
        )

    # Validation Summary

    validation_summary = build_validation_summary(
        validation_issues,
    )

    reports.append(
        SummaryReport(
            title="VALIDATION SUMMARY",
            worksheet_name="Validation Summary",
            data=validation_summary,
        )
    )

    return reports