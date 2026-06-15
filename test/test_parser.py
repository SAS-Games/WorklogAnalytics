from worklog_analytics.parsers.description_parser import extract_tags


def test_extract_single_tag():
    tags = extract_tags(
        "{Project_Activities}"
    )

    assert tags == [
        "Project_Activities"
    ]


def test_extract_multiple_tags():
    tags = extract_tags(
        "{Studio_Meeting}\n{Suri}"
    )

    assert tags == [
        "Studio_Meeting",
        "Suri"
    ]