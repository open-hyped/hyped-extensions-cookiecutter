"""{{ cookiecutter.name }}

{{ cookiecutter.description }}
"""

from typing import TYPE_CHECKING

# list all imports
__all__ = [
    "DummyProcessor"
]

if TYPE_CHECKING:  # pragma: not covered

    # standard imports for static type checkers, linting and auto-completion
    # add your normal imports here
    from .nodes.dummy import DummyProcessor

else:
    import sys

    from hyped.common.lazy_module import LazyModule

    # lazy imports
    _lazy_imports = {
        "DummyProcessor": "hyped.extensions.{{ cookiecutter.slug }}.nodes.dummy",
    }

    sys.modules[__name__] = LazyModule(
        __name__,
        __doc__,
        globals()["__file__"],
        __spec__,
        lazy_imports=_lazy_imports,
    )
