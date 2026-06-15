from pathlib import Path

from worklog_analytics.engine import run_analysis
from worklog_analytics.loaders.config_loader import load_json
from worklog_analytics.models.analysis_context import AnalysisContext


def build_context()->AnalysisContext:

    tag_aliases = load_json(Path("config/tag_aliases.json"))
    project_aliases = load_json(Path("config/project_aliases.json"))
    activity_config = load_json(Path("config/activity_groups.json"))
    project_config = load_json(Path("config/projects.json"))
    reports_config = load_json(Path("config/reports.json"))

    worklogs, validation_issues = run_analysis(
        Path("input/timesheetsample.xls"),
        activity_config,
        project_config,
        tag_aliases,
        project_aliases,
    )

    return AnalysisContext(
        worklogs=worklogs,
        validation_issues=validation_issues,
        reports_config=reports_config,
        activity_config=activity_config,
        project_config=project_config,
    )
