from dataclasses import dataclass

@dataclass
class ForecastRequest:

    remaining_working_days: int
    hours_per_day: float
    absence_plan: dict[str, int]
