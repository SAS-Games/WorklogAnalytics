from worklog_analytics.models.worklog import Worklog


def resolve_activity_group( worklog: Worklog,config: dict) -> tuple[str | None, str | None]:

    groups = config["activity_groups"]

    # Tags
    for group in groups:
        tags = group.get("tags",[])

        if any(tag in worklog.tags for tag in tags):
            return (group["name"],"Tag")
        
    # Summary Tags
    for group in groups:
        tags = group.get("tags", [])

        if any(tag in worklog.summary_tags for tag in tags):
            return (group["name"], "SummaryTag")

    # All Components
    for group in groups:
        components = group.get("components",[])

        if any( component in worklog.all_components for component in components):
            return (group["name"], "AllComponents" )

    # Component
    for group in groups:
        components = group.get( "components",[])

        if worklog.component in components:
            return (group["name"],"Component")

    return (None,None)