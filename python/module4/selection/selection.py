def process_data(records):
    cleaned = []
    for r in records:
        if r is not None and r != "" and r.strip() != "":
            cleaned.append(r.strip().lower())
    # ... more logic for filtering, transforming, exporting ...
    return cleaned