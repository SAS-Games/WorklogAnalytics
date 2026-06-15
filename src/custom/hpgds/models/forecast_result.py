from dataclasses import dataclass


@dataclass
class ForecastResult:

    actual_hours: float = 0.0

    forecast_hours: float = 0.0

    total_hours: float = 0.0
