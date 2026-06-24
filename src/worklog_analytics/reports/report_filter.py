def filter_worklogs(worklogs, filters: dict):

    result = []

    for worklog in worklogs:

        matched = True

        for field, value in filters.items():

            worklog_value = getattr(
                worklog,
                field,
                None,
            )

            if isinstance(value, list):

                if worklog_value not in value:
                    matched = False
                    break

            else:

                if worklog_value != value:
                    matched = False
                    break

        if matched:
            result.append(worklog)

    return result