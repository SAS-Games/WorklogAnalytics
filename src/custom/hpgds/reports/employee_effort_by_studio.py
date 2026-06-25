from collections import defaultdict
from custom.hpgds.constants import ACTIVITY_STUDIO_SUPPORT


def build_employee_effort_by_studio(worklogs, studio_groups_config) -> dict[str, dict[str, float]]:
    """
    Build a matrix of employee effort for each studio.
    
    Returns a nested dictionary:
    {
        "Studio Code": {
            "Employee Name": total_hours,
            ...
        },
        ...
    }
    """
    effort_matrix = defaultdict(lambda: defaultdict(float))

    # Initialize all studios from the config
    for group_studios in studio_groups_config.get("studio_groups", {}).values():
        for studio in group_studios:
            if studio not in effort_matrix:
                effort_matrix[studio] = defaultdict(float)

    # Add effort from worklogs
    for worklog in worklogs:
        # Only include studio support activities
        if worklog.activity_group != ACTIVITY_STUDIO_SUPPORT:
            continue

        # Skip if no project is assigned
        if worklog.project is None:
            continue

        # Use the project code directly as the studio
        studio = worklog.project

        # Add effort to the matrix
        effort_matrix[studio][worklog.employee] += worklog.hours

    # Convert defaultdict to regular dict for cleaner output
    return {studio: dict(employees) for studio, employees in effort_matrix.items()}
