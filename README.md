# yazio-sdk-python

[![Publish](https://github.com/yazio-community/yazio-sdk-python/actions/workflows/publish.yml/badge.svg)](https://github.com/yazio-community/yazio-sdk-python/actions/workflows/publish.yml)

A generated Python client for the private [YAZIO](https://www.yazio.com) API.

```bash
pip install yazio-sdk
```

> [!IMPORTANT]
> Unofficial and unaffiliated. YAZIO does not publish, endorse or support this
> client, and the API it targets is private: it can change without notice, and
> using it is subject to YAZIO's terms of service.

> [!NOTE]
> **`src/yazio_sdk/` is generated. Do not edit it.** It is produced from
> [yazio-api-specification](https://github.com/yazio-community/yazio-api-specification)
> by `openapi-python-client`, and the next spec release overwrites the whole
> tree. Bugs in the client's shape are bugs in the spec — report them there.
>
> It is tracked so the repository is installable at any commit — but it is
> written by CI, not committed by hand. The publish workflow regenerates it
> from each spec release and commits the result to `main` itself.
>
> Run `make generate` after cloning; the result is yours to run against, not
> to commit.

## Using it

Most endpoints need a bearer token, which you get by exchanging a username and
password for one. The OAuth client credentials are the mobile app's; they
identify the app, not you.

```python
from yazio_sdk import AuthenticatedClient, Client
from yazio_sdk.api.authentication import create_token
from yazio_sdk.models import OAuthTokenRequest

token = create_token.sync(
    client=Client(base_url="https://yzapi.yazio.com"),
    body=OAuthTokenRequest(
        username="me@example.com",
        password="…",
        client_id="3_5rbw4kehpugw8ogsc8ck8oo4ogswgckcskc04gcg8kk8k48ssw",
        client_secret="25gdtt1hvdi8gwowoww4oo88sgsw0oo04o0og0kkgwwks8k0k",
        grant_type="password",
    ),
)

client = AuthenticatedClient(
    base_url="https://yzapi.yazio.com",
    token=token.access_token,
    headers={
        # Required. See "The User-Agent gate" below — without this you get 403
        # on every endpoint.
        "user-agent": "YAZIO/26.30.1 (com.yazio.ios.YAZIO; build:2607271240; iOS 27.0.0) Ktor",
    },
)
```

Every endpoint module exposes four entry points, the generator's convention:

| Function | Returns |
| --- | --- |
| `sync(...)` | the parsed body, or `None` |
| `sync_detailed(...)` | a `Response` with status, headers and parsed body |
| `asyncio(...)` | the parsed body, awaited |
| `asyncio_detailed(...)` | the full `Response`, awaited |

```python
from yazio_sdk.api.products import search_products

results = search_products.sync(
    client=client,
    query="olive oil",
    sex="male",       # required by the API, not optional
    countries="de",   # ditto
)
```

Endpoints are grouped by tag under `yazio_sdk.api.<tag>`: `products`, `diary`,
`recipes`, `body_values`, `activity`, `goals`, `user`, and so on. Models live in
`yazio_sdk.models`.

## Things that will bite you

These are properties of the API, not of this client. The full list is in the
[spec repo's README](https://github.com/yazio-community/yazio-api-specification#things-the-api-does-not-document).

- **The User-Agent gate.** The API rejects any request whose client version it
  does not recognise with `403 {"error":"version_blocked"}`, on every endpoint
  except the token exchange, and the version travels in the User-Agent. Set it
  on the client as above. A wall of 403s means the string needs bumping.
- **Product nutrients are per one base unit, not per 100.** Olive oil reads 8.84
  kcal per gram. Getting this wrong scales every total by 100.
- **`sex` and `countries` are required on product search**, despite being
  typed optional-looking in older spec releases.
- **Deleting a diary entry** takes a body of `{"<bucket>": "<uuid>"}` — a single
  string, not a list — and answers `204` whether or not it deleted anything.

## Which spec a build came from

The package version **is** the spec version — `yazio-sdk==1.4.2` is generated
from spec release `v1.4.2`, always. There is no separate SDK version line to
cross-reference.

```python
import yazio_sdk
yazio_sdk.__version__       # '1.4.2'
yazio_sdk.__spec_version__  # '1.4.2' — the same string, by construction
```

That holds because nothing writes the version by hand. `scripts/generate.sh`
reads `info.version` out of `spec/openapi.yaml` and writes
`src/yazio_sdk/_version.py`; hatchling reads the version back from there at
build time. `pyproject.toml` declares it `dynamic`.

A rebuild with no spec change — a generator upgrade, a packaging fix — ships as
a PEP 440 post-release of the same spec version, `1.4.2.post1`.

## Development

```bash
nix-shell
make generate   # build src/yazio_sdk/ from spec/openapi.yaml — do this first
make sync       # fetch the latest spec release, then regenerate
make version    # what this checkout would publish as
make check      # what CI runs: generate, lint
```

`make check` failing on a diff means either the generated tree was edited by
hand or a spec was committed without regenerating. Both are fixed by
`make generate` and committing the result.

There is no test suite. `scripts/generate.sh` imports every module it wrote as
its last step, so generating is the smoke test, and the publish workflow
additionally imports the generated package under both ends of the supported
Python range.

Releases are fully automated, with no review step. When the spec repo tags a
release it dispatches here, and `.github/workflows/publish.yml` regenerates
from that spec, imports every module on Python 3.10 and 3.13, then commits to
`main`, tags `vX.Y.Z`, uploads to PyPI via trusted publishing and cuts the
GitHub release — one run, no human in the loop.

**There is no version to set.** It comes from the spec's `info.version`, so the
published version equals the spec release by construction. A spec that pins a
version already tagged here is refused before anything is written, and a
checkout generated from an unreleased spec reports `0.0.0-dev` and is refused
too.

The `src/` diff of a regeneration is the whole tree and says nothing useful, so
the run summary and the release body carry a **public surface diff** instead:
every client function and model as callers import them, before and after. A
removal or rename there is a breaking change, and it says so — after the fact,
which is the trade for having no review step.

## Licence

[MIT](LICENSE).
