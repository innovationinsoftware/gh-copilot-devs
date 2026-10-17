
from collections import Counter
from typing import Hashable, Iterable, List, TypeVar

T = TypeVar("T", bound=Hashable)


def find_duplicates(items: Iterable[T]) -> List[T]:
    counts = Counter(items)
    return [item for item, count in counts.items() if count > 1]
