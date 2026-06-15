from collections import defaultdict


def build_employee_forecast(
    worklogs,
    forecast_request
):

    employee_actuals = defaultdict(
        lambda: defaultdict(float)
    )

    # --------------------------------
    # Build employee distributions
    # --------------------------------

    for worklog in worklogs:

        category = None

        if worklog.activity_group == "Studio Support":

            category = worklog.project

        elif worklog.activity_group == "Project Activities":

            category = "Internal Activities"

        elif worklog.activity_group == "Org Activities":

            category = "Org Activities"

        elif worklog.activity_group == "Absense":

            category = "Absense"

        if category is not None:

            employee_actuals[
                worklog.employee
            ][category] += (
                worklog.hours
            )

    # --------------------------------
    # Forecast
    # --------------------------------

    forecast = defaultdict(
        lambda: defaultdict(float)
    )

    for employee, categories in (
        employee_actuals.items()
    ):

        productive_hours = sum(
            hours
            for category, hours in categories.items()
            if category != "Absense"
        )

        if productive_hours <= 0:
            continue

        absence_days = (
            forecast_request.absence_plan.get(
                employee,
                0
            )
        )

        productive_capacity = (
            forecast_request.remaining_working_days
            - absence_days
        ) * forecast_request.hours_per_day

        absence_capacity = (
            absence_days
            * forecast_request.hours_per_day
        )

        # -----------------------------
        # Productive Forecast
        # -----------------------------

        for category, actual_hours in (
            categories.items()
        ):

            if category == "Absense":
                continue

            percentage = (
                actual_hours
                / productive_hours
            )

            forecast[
                employee
            ][category] = (
                productive_capacity
                * percentage
            )

        # -----------------------------
        # Absense Forecast
        # -----------------------------

        if absence_capacity > 0:

            forecast[
                employee
            ]["Absense"] = (
                absence_capacity
            )

    return forecast