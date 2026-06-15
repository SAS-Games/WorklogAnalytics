import re

TAG_PATTERN = re.compile(r"\{([^}]*)\}")

def extract_tags(description: str, tag_alias_config: dict) -> list[str]:

    if not description:
        return []

    aliases = tag_alias_config.get("aliases", {})

    tags = []
    for tag in TAG_PATTERN.findall(description):
        tag = tag.strip()
        tag = aliases.get(tag, tag)
        tags.append(tag)

    return tags