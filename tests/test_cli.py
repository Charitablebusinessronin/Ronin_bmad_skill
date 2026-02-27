import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

import bmad_cli


def run_cli(argv):
    """Helper to execute the CLI and capture stdout/stderr for assertions."""
    stdout = io.StringIO()
    stderr = io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        exit_code = bmad_cli.main(argv)
    return exit_code, stdout.getvalue().strip(), stderr.getvalue().strip()


class TestBmadCLI(unittest.TestCase):
    def test_greet_success(self):
        exit_code, stdout, stderr = run_cli(["greet", "Alice"])
        self.assertEqual(exit_code, 0)
        self.assertEqual("Hello, Alice! Welcome to the BMAD CLI.", stdout)
        self.assertEqual("", stderr)

    def test_greet_trims_whitespace(self):
        exit_code, stdout, _ = run_cli(["greet", "  Bob  "])
        self.assertEqual(exit_code, 0)
        self.assertIn("Hello, Bob! Welcome to the BMAD CLI.", stdout)

    def test_rejects_empty_name(self):
        exit_code, _, stderr = run_cli(["greet", "    "])
        self.assertEqual(exit_code, 2)
        self.assertIn("Name cannot be empty.", stderr)

    def test_rejects_numeric_characters(self):
        exit_code, _, stderr = run_cli(["greet", "Alice1"])
        self.assertEqual(exit_code, 2)
        self.assertIn("Name cannot contain numbers.", stderr)

    def test_rejects_long_name(self):
        long_name = "A" * (bmad_cli.MAX_NAME_LENGTH + 1)
        exit_code, _, stderr = run_cli(["greet", long_name])
        self.assertEqual(exit_code, 2)
        self.assertIn("characters or fewer", stderr)

    def test_rejects_trailing_punctuation(self):
        exit_code, _, stderr = run_cli(["greet", "Alex-"])
        self.assertEqual(exit_code, 2)
        self.assertIn("Name cannot end with punctuation.", stderr)

    def test_rejects_consecutive_spaces(self):
        exit_code, _, stderr = run_cli(["greet", "Mary  Ann"])
        self.assertEqual(exit_code, 2)
        self.assertIn("consecutive spaces", stderr)


if __name__ == "__main__":
    unittest.main()
