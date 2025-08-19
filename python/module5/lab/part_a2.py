def format_name(first, last, title=""):
    if title:
        return f"{title} {first} {last}"
    return f"{first} {last}"

result = format_name("Grace")
print(result)
