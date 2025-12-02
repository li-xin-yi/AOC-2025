"""Utility functions shared across Advent of Code solutions."""

from pathlib import Path
import hashlib


def read_input(name: str) -> list[str]:
    """Reads lines from the given input txt file."""
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    return (script_dir / f"{name}.txt").read_text().strip().splitlines()


def md5(text: str) -> str:
    """Converts string to md5 hash."""
    return hashlib.md5(text.encode()).hexdigest()
