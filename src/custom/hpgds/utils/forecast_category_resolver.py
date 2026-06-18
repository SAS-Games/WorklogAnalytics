import custom.hpgds.constants as constants

def resolve_forecast_category(worklog):

    if worklog.activity_group == constants.ACTIVITY_STUDIO_SUPPORT:
        return worklog.project

    if worklog.activity_group == constants.ACTIVITY_PROJECT:
        return constants.CATEGORY_INTERNAL

    if worklog.activity_group == constants.ACTIVITY_ORG:
        return constants.CATEGORY_ORG

    if worklog.activity_group == constants.ACTIVITY_ABSENSE:
        return constants.CATEGORY_ABSENSE

    return None