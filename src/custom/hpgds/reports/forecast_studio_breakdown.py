from collections import defaultdict


def build_forecast_studio_breakdown(employee_forecast, actual_breakdown):

    summary = {}
    forecast_totals = defaultdict(float)

    for categories in employee_forecast.values():
        for category, hours in categories.items():
            if category in ("Internal Activities", "Org Activities", "Absense"):
                continue

            forecast_totals[category] += hours

    # Preserve actual breakdown order
    for project in actual_breakdown:
        summary[project] = forecast_totals.get(project, 0.0)

    return summary
