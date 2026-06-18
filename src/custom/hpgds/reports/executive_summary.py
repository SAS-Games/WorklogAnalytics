from custom.hpgds.utils.studio_group_resolver import resolve_studio_group
import custom.hpgds.constants as constants


def build_executive_summary(worklogs, studio_groups_config) -> dict[str, float]:

    summary = {}

    # --------------------------------
    # Studio Support Groups
    # --------------------------------

    for group_name in studio_groups_config["studio_groups"]:
        summary[f"{group_name}{constants.SUPPORT_SUFFIX}"] = 0.0

    # --------------------------------
    # Other Categories
    # --------------------------------

    summary[f"{constants.CATEGORY_INTERNAL}"] = 0.0
    summary[f"{constants.CATEGORY_ORG}"] = 0.0
    summary[f"{constants.CATEGORY_ABSENSE}"] = 0.0

    # --------------------------------
    # Aggregate
    # --------------------------------

    for worklog in worklogs:
        activity = worklog.activity_group

        if activity == f"{constants.ACTIVITY_PROJECT}":
            summary[f"{constants.CATEGORY_INTERNAL}"] += worklog.hours
            continue

        if activity == f"{constants.ACTIVITY_ORG}":
            summary[f"{constants.CATEGORY_ORG}"] += worklog.hours
            continue

        if activity == f"{constants.ACTIVITY_ABSENSE}":
            summary[f"{constants.CATEGORY_ABSENSE}"] += worklog.hours
            continue

        if activity == f"{constants.ACTIVITY_STUDIO_SUPPORT}":
            studio_group = resolve_studio_group(worklog.project, studio_groups_config)
            if studio_group is not None:
                summary[f"{studio_group}{constants.SUPPORT_SUFFIX}"] += worklog.hours

    return summary
