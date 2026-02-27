#!/usr/bin/env python3
"""BMAD CLI tool providing greeting utility."""

from __future__ import annotations

import argparse
import re
import sys
from typing import Iterable

__version__ = "0.1.0"

NAME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z\s\-']*$")
MAX_NAME_LENGTH = 50
INVALID_CHAR_MESSAGE = "Name must contain only letters, spaces, hyphens, or apostrophes."
REPEATED_SEPARATORS = {
    "  ": "consecutive spaces",
    "--": "consecutive hyphens",
    "''": "consecutive apostrophes",
}


class CLIError(Exception):
    """Raised when CLI input validation fails."""


def build_parser() -> argparse.ArgumentParser:
    """Configure the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="bmad-cli",
        description="A minimal BMAD helper CLI with a friendly greeter.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Display version information and exit.",
    )

    subparsers = parser.add_subparsers(dest="command", metavar="<command>")

    greet_parser = subparsers.add_parser(
        "greet", help="Greet someone by name with a friendly message."
    )
    greet_parser.add_argument("name", help="The name of the person to greet.")
    greet_parser.set_defaults(func=handle_greet)

    return parser


def validate_name(name: str) -> str:
    """Validate the name argument for the greet command."""
    cleaned = name.strip()
    if not cleaned:
        raise CLIError("Name cannot be empty.")
    if len(cleaned) > MAX_NAME_LENGTH:
        raise CLIError(f"Name must be {MAX_NAME_LENGTH} characters or fewer.")
    if any(char.isdigit() for char in cleaned):
        raise CLIError("Name cannot contain numbers.")
    for sequence, description in REPEATED_SEPARATORS.items():
        if sequence in cleaned:
            raise CLIError(f"Name cannot contain {description}.")
    if cleaned[-1] in {"-", "'"}:
        raise CLIError("Name cannot end with punctuation.")
    if not NAME_PATTERN.fullmatch(cleaned):
        raise CLIError(INVALID_CHAR_MESSAGE)
    return cleaned


def handle_greet(args: argparse.Namespace) -> int:
    """Execute the greet subcommand."""
    name = validate_name(args.name)
    print(f"Hello, {name}! Welcome to the BMAD CLI.")
    return 0


def main(argv: Iterable[str] | None = None) -> int:
    """Entry point for command-line execution."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not getattr(args, "command", None):
        parser.print_help()
        return 0

    try:
        return args.func(args)
    except CLIError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
