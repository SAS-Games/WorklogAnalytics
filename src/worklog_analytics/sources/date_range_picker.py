from datetime import datetime
from worklog_analytics.models.date_range import DateRange


def pick_date_range() -> DateRange:
    start = input("Start Date (YYYY-MM-DD): ")
    end = input("End Date (YYYY-MM-DD): ")

    return DateRange(
        start_date=datetime.strptime(start, "%Y-%m-%d").date(),
        end_date=datetime.strptime(end, "%Y-%m-%d").date(),
    )