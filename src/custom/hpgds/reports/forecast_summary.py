def build_forecast_summary(actual_summary, forecast):

    summary = {}

    for category in actual_summary:
        summary[category] = 0.0
        if category in forecast:
            summary[category] = forecast[category].forecast_hours

    return summary
