from pathlib import Path
from worklog_analytics.app import build_context
from worklog_analytics.loaders.config_loader import load_json
from worklog_analytics.reports.report_runner import run_reports
from worklog_analytics.reports.debug_report_runner import run_debug_reports
from custom.hpgds.reports.report_runner import run_hpgds_reports
from custom.hpgds.reports.review_items_report import run_review_items_report
from custom.hpgds.workbook.workbook_builder import generate_workbook
from custom.hpgds.loaders.forecast_loader import load_forecast_request
from custom.hpgds.validators.validate_hpgds_worklog import validate_hpgds_worklog
from custom.hpgds.utils.file_picker import pick_excel_file, pick_output_file
from worklog_analytics.sources.source_selector import (select_source,WorklogSourceType)
from worklog_analytics.sources.date_range_picker import pick_date_range
from worklog_analytics.sources.jira_downloader import download_jira_timesheet


def main():
    source = select_source()

    if source == WorklogSourceType.EXCEL:
        worklog_file = pick_excel_file("Select Worklog Excel File")
    else:
        date_range = pick_date_range()
        worklog_file = download_jira_timesheet(date_range)
    
    template_file = pick_excel_file("Select Report Template")
    output_file = pick_output_file()

    context = build_context(worklog_file)

    for worklog in context.worklogs:
        context.validation_issues.extend(validate_hpgds_worklog(worklog))

    studio_groups_config = load_json(Path("src/custom/hpgds/configs/studio_groups.json"), True)
    forecast_request = None
    forecast_config = load_json(Path("src/custom/hpgds/configs/forecast.json"), True)
    if forecast_config:
        forecast_request = load_forecast_request(forecast_config)

    run_reports(context)

    run_hpgds_reports(context.worklogs, context.validation_issues, studio_groups_config, forecast_request)
    run_debug_reports(context)
    run_review_items_report(context)
    generate_workbook(context.worklogs, context.validation_issues, studio_groups_config, template_file, output_file, forecast_request)


if __name__ == "__main__":
    main()
