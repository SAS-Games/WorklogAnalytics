from collections import defaultdict
from custom.hpgds.constants import CATEGORY_ABSENSE
from custom.hpgds.utils.forecast_category_resolver import resolve_forecast_category


def build_employee_forecast(worklogs, forecast_request):

    employee_actuals = defaultdict(lambda: defaultdict(float))

    # Build employee distributions

    for worklog in worklogs:
        category = resolve_forecast_category(worklog)
        if category is None:
            continue
        employee_actuals[worklog.employee][category] += worklog.hours

    # Forecast
    forecast = defaultdict(lambda: defaultdict(float))

    for employee, categories in employee_actuals.items():

        productive_hours = sum(
            hours
            for category, hours in categories.items()
            if category != CATEGORY_ABSENSE
        )

        if productive_hours <= 0:
            continue

        absence_days = forecast_request.absence_plan.get(employee, 0)

        productive_capacity = (
            forecast_request.remaining_working_days - absence_days
        ) * forecast_request.hours_per_day

        absence_capacity = absence_days * forecast_request.hours_per_day

        # Productive Forecast
        for category, actual_hours in categories.items():

            if category == CATEGORY_ABSENSE:
                continue

            percentage = actual_hours / productive_hours
            raw_forecast = productive_capacity * percentage
            forecast[employee][category] = round(round(raw_forecast * 4) / 4, 2)

        # Absense Forecast
        if absence_capacity > 0:
            forecast[employee][CATEGORY_ABSENSE] = round(round(absence_capacity * 4) / 4, 2)

    return forecast
