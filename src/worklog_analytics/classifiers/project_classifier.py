from worklog_analytics.models.worklog import Worklog
from worklog_analytics.classifiers.project_helper import (get_all_projects)


def normalize_project(project_name: str, aliases: dict) -> str:
    return aliases.get(project_name, project_name)


def resolve_project(worklog: Worklog, project_config: dict, project_aliases: dict) -> str | None:

    projects = get_all_projects(project_config)
    aliases = project_aliases.get("aliases", {})

    # Tags
    for tag in worklog.tags:
        normalized = normalize_project(tag, aliases)

        if normalized in projects:
            return normalized
        
    # Summary Tags
    for tag in worklog.summary_tags:
        normalized = normalize_project(tag, aliases)

        if normalized in projects:
            return normalized

    # All Components
    for component in worklog.all_components:
        normalized = normalize_project(component, aliases)

        if normalized in projects:
            return normalized

    # Primary Component
    normalized = normalize_project(worklog.component,aliases)
    if normalized in projects:
        return normalized

    return None