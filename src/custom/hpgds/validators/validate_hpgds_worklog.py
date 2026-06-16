from worklog_analytics.models.validation_issue import ValidationIssue
from worklog_analytics.models.worklog import Worklog
from custom.hpgds.constants import ACTIVITY_STUDIO_SUPPORT


def validate_hpgds_worklog(worklog: Worklog) -> list[ValidationIssue]:
    issues = []

    if worklog.activity_group == ACTIVITY_STUDIO_SUPPORT and worklog.project is None:

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
                reason="Studio Support Missing Project",
            )
        )

    return issues
