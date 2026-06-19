from pathlib import Path
from worklog_analytics.models.date_range import DateRange


def download_jira_timesheet(date_range: DateRange,
) -> Path:

    print(
        f"Downloading worklogs from "
        f"{date_range.start_date} to {date_range.end_date}"
    )

    #
    # TODO:
    # Call Jira API
    # Export to Excel
    #

    return Path("temp/worklogs.xlsx")