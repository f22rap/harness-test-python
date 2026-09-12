"""Trusted small sample for later workspace certification."""
def search(query: str, items: list[str]) -> list[str]:
    normalized=query.strip().casefold()
    if not normalized:
        return []
    return [item for item in items if normalized in item.casefold()]
