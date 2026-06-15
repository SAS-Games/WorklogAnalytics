from dataclasses import dataclass

from worklog_analytics.models.worklog import Worklog
from worklog_analytics.models.validation_issue import ValidationIssue


@dataclass
class AnalysisContext:

    worklogs: list[Worklog]

    validation_issues: list[ValidationIssue]

    reports_config: dict

    activity_config: dict

    project_config: dict