"""Hyped {{ cookiecutter.extension_name }} Extension

{{ cookiecutter.description }}
"""

from typing import TYPE_CHECKING
from .__version__ import __version__, __version_tuple__

# list all imports
__all__ = ["DummyProcessor"]

if TYPE_CHECKING:  # pragma: not covered
    # standard imports for static type checkers, linting and auto-completion
    # add your normal imports here
    from .nodes.dummy import DummyProcessor

else:
    import sys

    from hyped.common.lazy_module import LazyModule

    # lazy imports
    _lazy_imports = {
        "DummyProcessor": "hyped.extensions.{{ cookiecutter.extension_slug }}.nodes.dummy",
    }

    sys.modules[__name__] = LazyModule(
        __name__,
        __doc__,
        globals()["__file__"],
        __spec__,
        lazy_imports=_lazy_imports,
    )
    sys.modules[__name__].__version__ = __version__
    sys.modules[__name__].__version_tuple__ = __version_tuple__
