from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Worklog:
    issue_key: str
    employee: str
    work_date: datetime
    hours: float

    activity_name: str

    component: str
    all_components: list[str]

    work_description: str

    tags: list[str] = field(default_factory=list)
    summary_tags: list[str] = field(default_factory=list)

    activity_group: str | None = None
    project: str | None = None

    classification_source: str | None = None