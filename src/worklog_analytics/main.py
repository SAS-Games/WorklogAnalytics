from worklog_analytics.app import (build_context)
from worklog_analytics.reports.report_runner import (run_reports)
from worklog_analytics.reports.debug_report_runner import (run_debug_reports)


def main():

    context = build_context()
    run_reports(context)
    run_debug_reports(context)


if __name__ == "__main__":
    main()