def build_studio_support_breakdown(worklogs,studio_groups_config) -> dict[str, float]:

    summary = {}

    for projects in (studio_groups_config["studio_groups"].values()):
        for project in projects:
            summary[project] = 0.0


    for worklog in worklogs:

        if (worklog.activity_group!= "Studio Support"):
            continue

        if worklog.project is None:
            continue

        summary[worklog.project] += worklog.hours

    return summary