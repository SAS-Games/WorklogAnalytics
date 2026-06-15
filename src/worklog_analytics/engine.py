from pathlib import Path

from worklog_analytics.loaders.excel_loader import load_excel
from worklog_analytics.loaders.worklog_mapper import row_to_worklog
from worklog_analytics.classifiers.activity_classifier import resolve_activity_group
from worklog_analytics.classifiers.project_classifier import resolve_project
from worklog_analytics.validators.worklog_validator import validate_worklog


def run_analysis(excel_path, activity_config, project_config, tag_aliases, project_aliases):
    df = load_excel(excel_path)

    worklogs = [
        row_to_worklog(row, tag_aliases)
        for _, row in df.iterrows()
    ]

    for worklog in worklogs:
        activity_group, source = (resolve_activity_group(worklog,activity_config))

        worklog.activity_group = activity_group
        worklog.classification_source = source
        worklog.project = ( resolve_project( worklog, project_config, project_aliases))

    validation_issues = []

    for worklog in worklogs:
        validation_issues.extend(validate_worklog(worklog))

    return (worklogs, validation_issues)