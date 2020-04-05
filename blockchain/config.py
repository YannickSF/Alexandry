
from __future__ import annotations
from typing import Optional


class Singleton(type):
    _instance: Optional[Singleton] = None

    def __call__(cls, name) -> Singleton:
        if cls._instance is None:
            cls._instance = super().__call__(name)
        return cls._instance


class _Config:
    pass


CONFIG = _Config()
