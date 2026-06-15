def get_all_projects(project_config: dict) -> set[str]:
    return set(project_config.get("projects", []))