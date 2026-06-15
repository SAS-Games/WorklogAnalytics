from custom.hpgds.models.forecast_request import ForecastRequest


def load_forecast_request(config: dict) -> ForecastRequest:

    return ForecastRequest(
        remaining_working_days=config["remaining_working_days"],
        hours_per_day=config.get("hours_per_day", 8),
        absence_plan=config.get("absence_plan", {}),
    )
