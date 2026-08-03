"""A client library for accessing YAZIO API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)

from ._version import SPEC_VERSION as __spec_version__  # noqa: E402
from ._version import __version__  # noqa: E402
