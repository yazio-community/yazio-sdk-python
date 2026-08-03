{ pkgs ? import <nixpkgs> { } }:

let
  python = pkgs.python3.withPackages (ps: [
    # Runtime dependencies of the generated package. Keep these in step with
    # [project].dependencies in pyproject.toml — this shell is what local work
    # runs against, that list is what users install.
    ps.attrs
    ps.httpx
    ps.python-dateutil # generated date/date-time (de)serialisation

    # scripts/generate.sh reads info.version out of the spec to version the
    # package. Not a runtime dependency of the generated code.
    ps.pyyaml

    # `make docs`. Needs to be in *this* interpreter rather than alongside it:
    # pdoc imports the package to document it, so it has to see attrs, httpx
    # and dateutil on the same path.
    ps.pdoc
  ]);
in
pkgs.mkShell {
  name = "yazio-sdk-python";

  packages = [
    python
    pkgs.openapi-python-client # turns spec/openapi.yaml into src/yazio_sdk/
    # The generator runs this over its own output as a post-hook, so its
    # version is an input to the generated tree rather than just a linter.
    # The workflows pin the same version explicitly; if nixpkgs moves, update
    # the pin in pyproject.toml and .github/workflows/ to match, or CI and
    # local will format the generated code differently.
    pkgs.ruff
    pkgs.hatch # `hatch version` resolves the dynamic version from _version.py
  ];

  # src layout: the package is not installed in this shell, it is imported from
  # the tree, which is also what makes a freshly generated tree testable before
  # anything is built.
  shellHook = ''
    export PYTHONPATH="$PWD/src''${PYTHONPATH:+:$PYTHONPATH}"

    echo "yazio-sdk-python dev shell"
    echo "  openapi-python-client    ${pkgs.openapi-python-client.version}"
    echo
    echo "  make generate   rebuild src/yazio_sdk/ from spec/openapi.yaml"
    echo "  make sync       pull the latest spec release, then regenerate"
    echo "  make version    print the version this checkout would publish"
    echo "  make docs       render HTML API docs to \$DOCS_DIR (default /tmp)"
  '';
}
