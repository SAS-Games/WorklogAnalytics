from dataclasses import dataclass


@dataclass
class EmployeeForecast:
    employee: str
    forecast_hours: dict[str, float]