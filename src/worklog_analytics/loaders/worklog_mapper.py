from worklog_analytics.models.worklog import Worklog
from worklog_analytics.parsers.tag_parser import extract_tags


def row_to_worklog( row,tag_alias_config: dict) -> Worklog:

    description = str(row["Work Description"])

    return Worklog(
        issue_key=row["Issue Key"],
        employee=row["Full name"],
        work_date=row["Work date"],
        hours=float(row["Hours"]),

        activity_name=str(
            row["Activity Name"]
        ),

        component=str(
            row["Component"]
        ),

        all_components=[
            c.strip()
            for c in str(
                row["All Components"]
            ).split(";")
            if c.strip()
        ],

        work_description=description,

        tags=extract_tags(
            description,
            tag_alias_config
        )
    )