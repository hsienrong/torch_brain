from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("torch_brain")
except PackageNotFoundError:  # pragma: no cover
    # This can happen if someone is importing the package without installing
    __version__ = "0.2.1-hsien"  # pragma: no cover
