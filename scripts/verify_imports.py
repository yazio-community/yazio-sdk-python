#!/usr/bin/env python3
"""Import every module in the generated package and report all failures at once.

This is the whole test suite. The package is generated, so testing its
behaviour would be testing openapi-python-client; what is worth checking is
that a release is importable at all, and that is exactly what breaks when a
spec change produces a name collision or an unresolvable reference.

It lives in its own file rather than inside scripts/generate.sh because the two
run under different Python versions. openapi-python-client requires >=3.11, but
the generated package supports >=3.10 — so CI generates on 3.12 and then runs
this on both ends of the supported range.

Usage:  python3 scripts/verify_imports.py [package-name]
"""

import importlib
import pkgutil
import sys


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else "yazio_sdk"

    try:
        package = importlib.import_module(name)
    except Exception as exc:  # noqa: BLE001 - the message is the whole point
        sys.exit(f"error: cannot import {name}: {exc}")

    failed = []
    for module in pkgutil.walk_packages(package.__path__, f"{package.__name__}."):
        try:
            importlib.import_module(module.name)
        except Exception as exc:  # noqa: BLE001 - report every broken module at once
            failed.append(f"{module.name}: {exc}")

    if failed:
        sys.exit("import errors:\n  " + "\n  ".join(failed))

    version = getattr(package, "__version__", "?")
    spec_version = getattr(package, "__spec_version__", "?")
    print(
        f"ok: {name} {version} from spec {spec_version} "
        f"on Python {sys.version_info.major}.{sys.version_info.minor}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
