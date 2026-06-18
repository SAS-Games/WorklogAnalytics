from collections import defaultdict
import custom.hpgds.constants as constants


def build_forecast_studio_breakdown(employee_forecast, actual_breakdown):

    forecast_totals = defaultdict(float)

    for categories in employee_forecast.values():

        for category, hours in categories.items():

            if category in (
                constants.CATEGORY_INTERNAL,
                constants.CATEGORY_ORG,
                constants.CATEGORY_ABSENSE,
            ):
                continue

            forecast_totals[category] += hours

    summary = {}

    # Preserve actual report order

    for project in actual_breakdown:

        summary[project] = forecast_totals.get(project, 0.0)

    return summary
