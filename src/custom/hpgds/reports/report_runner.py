from custom.hpgds.reports.executive_summary import build_executive_summary
from custom.hpgds.reports.studio_support_breakdown import build_studio_support_breakdown
from custom.hpgds.reports.validation_summary import build_validation_summary
from custom.hpgds.reports.hpgds_forecast import build_hpgds_forecast
from custom.hpgds.reports.forecast_summary import build_forecast_summary
from custom.hpgds.reports.final_summary import build_final_summary
from custom.hpgds.reports.summary_printer import print_summary
from custom.hpgds.reports.forecast_studio_breakdown import (build_forecast_studio_breakdown,)
from custom.hpgds.reports.final_studio_breakdown import build_final_studio_breakdown
from custom.hpgds.calculators.employee_forecast_builder import build_employee_forecast


def run_hpgds_reports(worklogs, validation_issues, studio_groups_config, forecast_request=None):

    # Actual Summary
    actual_summary = build_executive_summary(worklogs, studio_groups_config)
    print_summary("HP-GDS EFFORT SUMMARY", actual_summary)

    # Actual Studio Breakdown
    studio_breakdown = build_studio_support_breakdown(worklogs, studio_groups_config)
    print("\n=========== STUDIO SUPPORT BREAKDOWN ===========\n")
    for project, hours in studio_breakdown.items():
        print(f"{project}: " f"{hours:.2f}h")

    # Forecast Reports (Optional)
    if forecast_request is not None:
        employee_forecast = build_employee_forecast(worklogs, forecast_request)
        
        # HP-GDS Forecast
        forecast = build_hpgds_forecast(worklogs, studio_groups_config, employee_forecast)
        forecast_summary = build_forecast_summary(actual_summary, forecast)
        print_summary("HP-GDS FORECASTED EFFORT SUMMARY", forecast_summary)
        
        final_summary = build_final_summary(actual_summary, forecast)
        print_summary("HP-GDS FINAL EFFORT SUMMARY", final_summary)

        # Studio Forecast Breakdown
        forecast_breakdown = build_forecast_studio_breakdown(employee_forecast, studio_breakdown)
        print("\n=========== FORECASTED STUDIO SUPPORT BREAKDOWN ===========\n")
        for project, hours in forecast_breakdown.items():
            print(f"{project}: " f"{hours:.2f}h")

        final_breakdown = build_final_studio_breakdown(studio_breakdown, forecast_breakdown)
        print("\n=========== FINAL STUDIO SUPPORT BREAKDOWN ===========\n")
        for project, hours in final_breakdown.items():
            print(f"{project}: " f"{hours:.2f}h")

    # Validation Summary
    validation_summary = build_validation_summary(validation_issues)
    print("\n=========== VALIDATION SUMMARY ===========\n")
    for reason, hours in validation_summary.items():
        print(f"{reason}: " f"{hours:.2f}h")
