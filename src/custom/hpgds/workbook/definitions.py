from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class ReportDefinition:
    sheet_name: str
    data: Any
    writer: Callable