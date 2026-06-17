from collections.abc import Iterable
from typing import Hashable, TypeVar


T = TypeVar("T", bound=Hashable)


def find_duplicates(items: Iterable[T]) -> list[T]:
    seen: set[T] = set()
    duplicate_set: set[T] = set()
    duplicates: list[T] = []

    for item in items:
        if item in seen:
            if item not in duplicate_set:
                duplicate_set.add(item)
                duplicates.append(item)
        else:
            seen.add(item)

    return duplicates


numbers = [4, 7, 2, 4, 9, 2, 1, 7, 3, 2]
print("Duplicate numbers:", find_duplicates(numbers))

words = ["apple", "banana", "apple", "orange", "banana", "grape"]
print("Duplicate words:", find_duplicates(words))