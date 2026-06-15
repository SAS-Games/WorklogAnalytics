from collections import defaultdict

from custom.hpgds.models.forecast_result import ForecastResult

from custom.hpgds.utils.studio_group_resolver import resolve_studio_group


def build_hpgds_forecast(worklogs, studio_groups_config, forecast_request):

    employee_actuals = defaultdict(lambda: defaultdict(float))

    # -----------------------------
    # Build employee distributions
    # -----------------------------

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

            employee_actuals[worklog.employee][category] += worklog.hours

    # -----------------------------
    # Aggregate Forecast
    # -----------------------------

    forecast = defaultdict(ForecastResult)

    for employee, categories in employee_actuals.items():

        productive_hours = sum(
            hours for category, hours in (categories.items()) if category != "Absense"
        )

        if productive_hours <= 0:
            continue

        absence_days = forecast_request.absence_plan.get(employee, 0)

        productive_capacity = (
            forecast_request.remaining_working_days - absence_days
        ) * 8

        absence_capacity = absence_days * 8

        for category, actual_hours in categories.items():

            forecast[category].actual_hours += actual_hours

            if category == "Absense":
                continue

            percentage = actual_hours / productive_hours

            forecast_hours = productive_capacity * percentage

            forecast[category].forecast_hours += forecast_hours

        forecast["Absense"].forecast_hours += absence_capacity

    # -----------------------------
    # Final Totals
    # -----------------------------

    for result in forecast.values():

        result.total_hours = result.actual_hours + result.forecast_hours

    return forecast
