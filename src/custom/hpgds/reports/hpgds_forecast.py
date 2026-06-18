from collections import defaultdict
from custom.hpgds.models.forecast_result import ForecastResult
import custom.hpgds.constants as constants
from custom.hpgds.utils.forecast_category_resolver import resolve_forecast_category
from custom.hpgds.utils.studio_group_resolver import resolve_studio_group


def build_hpgds_forecast(worklogs, studio_groups_config, employee_forecast):

    forecast = defaultdict(ForecastResult)

    # Actual Hours
    for worklog in worklogs:

        category = resolve_forecast_category(worklog)

        if category is None:
            continue

        if worklog.activity_group == constants.ACTIVITY_STUDIO_SUPPORT:

            studio_group = resolve_studio_group(worklog.project, studio_groups_config)
            if studio_group is not None:
                category = f"{studio_group}" f"{constants.SUPPORT_SUFFIX}"

        forecast[category].actual_hours += worklog.hours

    # Forecast Hours
    for categories in employee_forecast.values():
        for category, hours in categories.items():
            studio_group = resolve_studio_group(category, studio_groups_config)

            if studio_group is not None:
                category = f"{studio_group}" f"{constants.SUPPORT_SUFFIX}"

            forecast[category].forecast_hours += hours

    # Totals
    for result in forecast.values():
        result.total_hours = result.actual_hours + result.forecast_hours

    return forecast
