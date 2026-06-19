from enum import Enum

class WorklogSourceType(Enum):
    EXCEL = "excel"
    JIRA = "jira"


def select_source() -> WorklogSourceType:
    print("\nWorklog Source")
    print("1. Excel")
    print("2. Jira")

    choice = input("Select Source: ")

    if choice == "2":
        return WorklogSourceType.JIRA

    return WorklogSourceType.EXCEL
