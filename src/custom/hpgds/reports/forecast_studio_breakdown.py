from collections import defaultdict

from custom.hpgds.constants import (
    CATEGORY_INTERNAL,
    CATEGORY_ORG,
    CATEGORY_ABSENSE,
)


def build_forecast_studio_breakdown(employee_forecast, actual_breakdown):

    forecast_totals = defaultdict(float)

    for categories in employee_forecast.values():

        for category, hours in categories.items():

            if category in (
                CATEGORY_INTERNAL,
                CATEGORY_ORG,
                CATEGORY_ABSENSE,
            ):
                continue

            forecast_totals[category] += hours

    summary = {}

    # Preserve actual report order

    for project in actual_breakdown:

        summary[project] = forecast_totals.get(project, 0.0)

    return summary
