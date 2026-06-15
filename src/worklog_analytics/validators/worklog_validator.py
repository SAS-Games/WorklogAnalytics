from worklog_analytics.models.validation_issue import (ValidationIssue)
from worklog_analytics.models.worklog import (Worklog)


def validate_worklog(worklog: Worklog) -> list[ValidationIssue]:

    issues = []

    # Activity Group Missing
    if worklog.activity_group is None:

        issues.append(
            ValidationIssue(
                issue_key=worklog.issue_key,
                employee=worklog.employee,
                hours=worklog.hours,
                activity_name=worklog.activity_name,
                activity_group=worklog.activity_group,
                project=worklog.project,
                component=worklog.component,
                all_components=worklog.all_components,
                tags=worklog.tags,
                reason="Activity Group Not Found"
            )
        )

    # Studio Support Requires Project
    if (worklog.activity_group == "Studio Support" and worklog.project is None):

        issues.append(
            ValidationIssue(
                issue_key=worklog.issue_key,
                employee=worklog.employee,
                hours=worklog.hours,
                activity_name=worklog.activity_name,
                activity_group=worklog.activity_group,
                project=worklog.project,
                component=worklog.component,
                all_components=worklog.all_components,
                tags=worklog.tags,
                reason="Studio Support Missing Project"
            )
        )

    return issues