# from core.types import *
# from typing import Any


class StringFormat:

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "text1": ("STRING", {"multiline": False, "default": "Hello"}),
            "text2": ("STRING", {"multiline": False, "default": "World"}),
        }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate_text"
    CATEGORY = "🧩 Tutorial Nodes"

    def concatenate_text(self, text1, text2):
        text_out = text1 + " " + text2
        return (text_out,)
