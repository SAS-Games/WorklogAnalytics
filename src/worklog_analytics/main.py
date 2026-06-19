from worklog_analytics.app import (build_context)
from worklog_analytics.reports.report_runner import (run_reports)
from worklog_analytics.reports.debug_report_runner import (run_debug_reports)
from worklog_analytics.sources.source_selector import (select_source,WorklogSourceType)
from worklog_analytics.sources.date_range_picker import pick_date_range
from worklog_analytics.sources.jira_downloader import download_jira_timesheet

def main():

    source = select_source()
    if source == WorklogSourceType.EXCEL:
        worklog_file = "input/timesheetsample.xls";
    else:
        date_range = pick_date_range()
        worklog_file = download_jira_timesheet(date_range)
    
    context = build_context(worklog_file)
    run_reports(context)
    run_debug_reports(context)


if __name__ == "__main__":
    main()