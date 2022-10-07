from dataclasses import dataclass


@dataclass
class Example:
    """Example class for package_name."""

    name: str = "example"

    def name_reversed(self) -> str:
        """Return `name` backwards."""
        return self.name[::-1]
