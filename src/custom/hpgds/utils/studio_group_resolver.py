def resolve_studio_group(project: str | None, config: dict) -> str | None:

    if project is None:
        return None

    for group_name, projects in config["studio_groups"].items():
        if project in projects:
            return group_name

    return None
