from collections import defaultdict

from custom.hpgds.models.forecast_result import ForecastResult

from custom.hpgds.utils.studio_group_resolver import resolve_studio_group


def build_hpgds_forecast(worklogs, studio_groups_config, employee_forecast):

    forecast = defaultdict(ForecastResult)

    # --------------------------------
    # Actual Hours
    # --------------------------------

    for worklog in worklogs:

        category = None

        if worklog.activity_group == "Project Activities":
            category = "Internal Activities"

        elif worklog.activity_group == "Org Activities":
            category = "Org Activities"

        elif worklog.activity_group == "Studio Support":

            studio_group = resolve_studio_group(worklog.project, studio_groups_config)

            if studio_group:

                category = f"{studio_group} Support"

        elif worklog.activity_group == "Absense":

            category = "Absense"

        if category is not None:

            forecast[category].actual_hours += worklog.hours

    # --------------------------------
    # Forecast Hours
    # --------------------------------

    for employee, categories in employee_forecast.items():

        for category, hours in categories.items():

            studio_group = resolve_studio_group(category, studio_groups_config)

            if studio_group is not None:

                forecast[f"{studio_group} Support"].forecast_hours += hours

            else:

                forecast[category].forecast_hours += hours

    # --------------------------------
    # Totals
    # --------------------------------

    for result in forecast.values():

        result.total_hours = result.actual_hours + result.forecast_hours

    return forecast
