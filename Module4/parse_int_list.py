def parse_int_list(s: str) -> list[int]:
    return [int(x) for x in s.split(",")]


parse_int_list("1, 2, 3")