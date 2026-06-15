from custom.hpgds.utils.studio_group_resolver import resolve_studio_group


def build_executive_summary(worklogs, studio_groups_config) -> dict[str, float]:

    summary = {}

    # --------------------------------
    # Studio Support Groups
    # --------------------------------

    for group_name in studio_groups_config["studio_groups"]:
        summary[f"{group_name} Support"] = 0.0

    # --------------------------------
    # Other Categories
    # --------------------------------

    summary["Internal Activities"] = 0.0
    summary["Org Activities"] = 0.0
    summary["Absense"] = 0.0

    # --------------------------------
    # Aggregate
    # --------------------------------

    for worklog in worklogs:
        activity = worklog.activity_group

        if activity == "Project Activities":
            summary["Internal Activities"] += worklog.hours
            continue

        if activity == "Org Activities":
            summary["Org Activities"] += worklog.hours
            continue

        if activity == "Absense":
            summary["Absense"] += worklog.hours
            continue

        if activity == "Studio Support":
            studio_group = resolve_studio_group(worklog.project, studio_groups_config)
            if studio_group is not None:
                summary[f"{studio_group} Support"] += worklog.hours

    return summary
