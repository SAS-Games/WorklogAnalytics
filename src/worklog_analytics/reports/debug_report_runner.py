from worklog_analytics.models.analysis_context import (AnalysisContext)

def run_debug_reports(context:AnalysisContext):

    worklogs = context.worklogs
    validation_issues = context.validation_issues

    # Sample Worklogs
    print("\n=========== FIRST 20 WORKLOGS ===========\n")
    for worklog in worklogs:

        print(
            f"{worklog.issue_key} | "
            f"{worklog.employee} | "
            f"{worklog.hours}h | "
            f"Tags={worklog.tags} | "
            f"Activity={worklog.activity_group} | "
            f"Project={worklog.project} | "
            f"Source={worklog.classification_source}"
        )

    # Validation Issues
    print("\n=========== VALIDATION ISSUES ===========\n")
    for issue in validation_issues:

        print(
            f"{issue.issue_key} | "
            f"{issue.employee} | "
            f"{issue.hours}h | "
            f"Activity={issue.activity_group} | "
            f"Project={issue.project} | "
            f"Reason={issue.reason} | "
            f"Tags={issue.tags} | "
            f"Component={issue.component} | "
            f"AllComponents={issue.all_components}"
        )