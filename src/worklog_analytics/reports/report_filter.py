def filter_worklogs(worklogs,filters: dict):
    result = []

    for worklog in worklogs:
        matched = True

        for field, value in filters.items():
            if getattr(worklog, field) != value:
                matched = False
                break

        if matched:
            result.append(worklog)

    return result