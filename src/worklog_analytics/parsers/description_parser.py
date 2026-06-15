import re


TAG_PATTERN = re.compile(r"\{([^}]*)\}")


def extract_tags(description: str) -> list[str]:
    """
    Extract tags from work description.

    Example:
    {Studio_Meeting}
    {Suri}

    Returns:
    ["Studio_Meeting", "Suri"]
    """

    if not description:
        return []

    return [
        tag.strip()
        for tag in TAG_PATTERN.findall(description)
        if tag.strip()
    ]