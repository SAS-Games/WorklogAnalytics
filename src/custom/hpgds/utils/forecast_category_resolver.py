from custom.hpgds.constants import (
    ACTIVITY_STUDIO_SUPPORT,
    ACTIVITY_PROJECT,
    ACTIVITY_ORG,
    ACTIVITY_ABSENSE,
    CATEGORY_INTERNAL,
    CATEGORY_ORG,
    CATEGORY_ABSENSE,
)


def resolve_forecast_category(worklog):

    if worklog.activity_group == ACTIVITY_STUDIO_SUPPORT:
        return worklog.project

    if worklog.activity_group == ACTIVITY_PROJECT:
        return CATEGORY_INTERNAL

    if worklog.activity_group == ACTIVITY_ORG:
        return CATEGORY_ORG

    if worklog.activity_group == ACTIVITY_ABSENSE:
        return CATEGORY_ABSENSE

    return None