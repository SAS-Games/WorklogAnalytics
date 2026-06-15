from collections import defaultdict


def build_summary(worklogs,group_by: str,include_none: bool = True, expected_values: list[str] | None = None,) -> dict[str, float]:

    summary = defaultdict(float)

    if expected_values:
        for value in expected_values:
            summary[value] = 0.0

    for worklog in worklogs:
        value = getattr(worklog, group_by, None)

        if value is None:
            if not include_none:
                continue

            value = f"No {group_by}"
        summary[value] += worklog.hours

    return dict(summary)
