from collections import defaultdict


def build_validation_summary(validation_issues) -> dict[str, float]:
    summary = defaultdict(float)

    for issue in validation_issues:
        summary[issue.reason] += issue.hours

    return dict(summary)