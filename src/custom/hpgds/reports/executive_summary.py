from custom.hpgds.utils.studio_group_resolver import resolve_studio_group
from custom.hpgds.constants import (
    ACTIVITY_PROJECT,
    ACTIVITY_STUDIO_SUPPORT,
    ACTIVITY_ORG,
    ACTIVITY_ABSENSE,
    CATEGORY_INTERNAL,
    CATEGORY_ORG,
    CATEGORY_ABSENSE,
    SUPPORT_SUFFIX)


def build_executive_summary(worklogs, studio_groups_config) -> dict[str, float]:

    summary = {}

    # --------------------------------
    # Studio Support Groups
    # --------------------------------

    for group_name in studio_groups_config["studio_groups"]:
        summary[f"{group_name}{SUPPORT_SUFFIX}"] = 0.0

    # --------------------------------
    # Other Categories
    # --------------------------------

    summary[f"{CATEGORY_INTERNAL}"] = 0.0
    summary[f"{CATEGORY_ORG}"] = 0.0
    summary[f"{CATEGORY_ABSENSE}"] = 0.0

    # --------------------------------
    # Aggregate
    # --------------------------------

    for worklog in worklogs:
        activity = worklog.activity_group

        if activity == f"{ACTIVITY_PROJECT}":
            summary[f"{CATEGORY_INTERNAL}"] += worklog.hours
            continue

        if activity == f"{ACTIVITY_ORG}":
            summary[f"{CATEGORY_ORG}"] += worklog.hours
            continue

        if activity == f"{ACTIVITY_ABSENSE}":
            summary[f"{CATEGORY_ABSENSE}"] += worklog.hours
            continue

        if activity == f"{ACTIVITY_STUDIO_SUPPORT}":
            studio_group = resolve_studio_group(worklog.project, studio_groups_config)
            if studio_group is not None:
                summary[f"{studio_group} Support"] += worklog.hours

    return summary
