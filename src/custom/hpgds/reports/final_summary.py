def build_final_summary(actual_summary, forecast) -> dict[str, float]:

    summary = {}

    for category in actual_summary:
        actual = actual_summary.get(category, 0.0)
        forecast_hours = 0.0

        if category in forecast:
            forecast_hours = forecast[category].forecast_hours

        summary[category] = actual + forecast_hours

    return summary
