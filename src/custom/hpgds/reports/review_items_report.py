from worklog_analytics.models.analysis_context import (AnalysisContext)

def run_review_items_report(context: AnalysisContext):

    worklogs = (context.worklogs)

    print( "\n=========== REVIEW ITEMS ===========\n")

    for worklog in worklogs:

        if (worklog.activity_group == "Project Activities" and worklog.project is not None):

            print(f"{worklog.issue_key} | " f"{worklog.employee} | " f"{worklog.hours}h | "
                f"Activity={worklog.activity_group} | "f"Project={worklog.project} | "
                f"Tags={worklog.tags} | " f"Component={worklog.component}"
            )