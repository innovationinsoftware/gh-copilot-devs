from dataclasses import dataclass, field
from typing import Any, Dict

# Product
@dataclass
class Widget:
    name: str
    size: int = 0
    color: str = "gray"
    config: Dict[str, Any] = field(default_factory=dict)

# Factory
class WidgetFactory:
    def create(self, name: str, size: int = 0, color: str = "gray", **config) -> Widget:
        return Widget(name=name, size=size, color=color, config=config)
