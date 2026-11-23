from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

__version__: str | None = None
try:
    __version__ = version("django-pipeline")
except PackageNotFoundError:
    pass
