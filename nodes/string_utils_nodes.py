from core.types import *
from typing import Any


class StringFormat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"any": Any},
            "optional": {"format": STRING}
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "format"
    CATEGORY = "xutils"

    def format(self, input, format: str):
        return (format.format(input),)
