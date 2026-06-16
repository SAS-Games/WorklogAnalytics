from pathlib import Path
from worklog_analytics.app import (build_context)
from worklog_analytics.loaders.config_loader import (load_json)
from worklog_analytics.reports.report_runner import (run_reports)
from worklog_analytics.reports.debug_report_runner import (run_debug_reports)
from custom.hpgds.reports.report_runner import (run_hpgds_reports)
from custom.hpgds.reports.review_items_report import ( run_review_items_report)
from custom.hpgds.excel.workbook_builder import (generate_workbook)
from custom.hpgds.loaders.forecast_loader import (load_forecast_request)
from custom.hpgds.validators.validate_hpgds_worklog import (validate_hpgds_worklog)

def main():

    context = build_context()
    for worklog in context.worklogs:
        context.validation_issues.extend(validate_hpgds_worklog(worklog))

    studio_groups_config = load_json(Path( "src/custom/hpgds/configs/studio_groups.json"))
    forecast_config = load_json(Path("src/custom/hpgds/configs/forecast.json"))

    run_reports(context)
    forecast_request = (load_forecast_request(forecast_config))
    run_hpgds_reports(context.worklogs, context.validation_issues, studio_groups_config, forecast_request)
    generate_workbook(context.worklogs, context.validation_issues, studio_groups_config, Path("output/worklog_report.xlsx"))
    run_debug_reports(context)
    run_review_items_report(context)


if __name__ == "__main__":
    main()