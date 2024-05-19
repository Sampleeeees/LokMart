"""Django Unfold module"""
import threading
import typing
from injector import Binder, Module, singleton


class DjangoUnfoldModule(Module):
    """Django Unfold Module"""

    def init(self) -> None:
        """Initialize."""
        self._local = threading.local()

    def configure(self, binder: Binder) -> None:
        """Configure."""
        binder.multibind(typing.Dict[str, typing.Any], to={}, scope=singleton)
        binder.multibind(typing.Dict[str, str], to={}, scope=singleton)