# =============================================================================
#  biotechnology.__main__
# -----------------------------------------------------------------------------
#  Enables `python -m biotechnology`.
#
#  WHY THIS FILE EXISTS SEPARATELY FROM THE CONSOLE SCRIPT
#  `pip install biotechnology` creates a `biotechnology` executable through the
#  console-scripts entry point declared in pyproject.toml. That is the normal
#  way to run the command line, and it is what the documentation shows.
#
#  It is not always available:
#
#    * On a fresh install the scripts directory may not be on PATH. This is
#      routine on Windows, and it is exactly the situation where a user who is
#      not a habitual programmer gives up. `python -m biotechnology` always
#      works, because it needs no PATH entry at all.
#    * In a locked-down environment - a teaching cluster, an air-gapped
#      analysis host, a hospital or regulatory review machine - the package may
#      be vendored onto sys.path rather than installed, so no entry point
#      exists.
#    * Inside a container or CI job it is often clearer to invoke the
#      interpreter explicitly, so that which Python is running is unambiguous.
#    * When several virtual environments are active in one shell, `python -m`
#      removes any doubt about which installation answered.
#
#  Both routes call exactly the same `cli.main`, so behaviour cannot diverge
#  between them.
#
#  EXIT CODES
#  `main()` returns an integer, which is passed to SystemExit unchanged:
#
#      0   success
#      1   a handled error - unknown path, no search match, failed validation
#      2   argparse usage error (raised by argparse itself, not by us)
#
#  These are stable and may be relied on in scripts and CI pipelines.
#
#  KEYBOARD INTERRUPT
#  Ctrl-C exits with 130, the conventional 128 + SIGINT, and prints nothing.
#  A Python traceback in response to a deliberate interrupt is noise, and for a
#  reference tool that a non-programmer may be exploring interactively it looks
#  like a crash.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import sys

from .cli import main

# -----------------------------------------------------------------------------
#  Conventional exit code for termination by SIGINT: 128 + 2.
#  Named rather than inlined so that the magic number is explained once.
# -----------------------------------------------------------------------------
_EXIT_INTERRUPTED = 130

# -----------------------------------------------------------------------------
#  Conventional exit code for a broken pipe. Reached when output is piped into
#  a command that stops reading early:
#
#      biotechnology tree | head -20
#
#  `head` closes the pipe after twenty lines; without this handling Python
#  reports "BrokenPipeError: [Errno 32]" on stderr and exits non-zero, which
#  makes a perfectly ordinary shell idiom look like a failure.
# -----------------------------------------------------------------------------
_EXIT_BROKEN_PIPE = 141


def _run() -> int:
    """Invoke the command line, translating signals into conventional codes."""
    try:
        return main()

    except KeyboardInterrupt:
        # Newline first, so the shell prompt does not land mid-line after the
        # partially written output that the interrupt cut off.
        print(file=sys.stderr)
        return _EXIT_INTERRUPTED

    except BrokenPipeError:
        # Python flushes stdout at interpreter shutdown, which would raise a
        # second BrokenPipeError and print a warning after we have already
        # decided to exit quietly. Redirecting the file descriptor to the null
        # device is the documented remedy.
        try:
            devnull = __import__("os").open(__import__("os").devnull, 1)
            __import__("os").dup2(devnull, sys.stdout.fileno())
        except Exception:  # noqa: BLE001 - best effort during shutdown
            pass
        return _EXIT_BROKEN_PIPE


# -----------------------------------------------------------------------------
#  The guard is required. Without it, `python -m biotechnology` would execute
#  the command line during the import that `runpy` performs to locate this
#  module, running it twice.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    raise SystemExit(_run())
