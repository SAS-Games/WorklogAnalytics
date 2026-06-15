from dataclasses import dataclass


@dataclass
class ValidationIssue:
    issue_key: str
    employee: str
    hours: float

    activity_name: str
    activity_group: str | None

    project: str | None

    component: str
    all_components: list[str]

    tags: list[str]

    reason: str