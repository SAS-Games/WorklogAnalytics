def build_final_studio_breakdown(actual_breakdown, forecast_breakdown):

    summary = {}

    for project in actual_breakdown:
        summary[project] = actual_breakdown.get(project, 0.0) + forecast_breakdown.get( project, 0.0)

    return summary
