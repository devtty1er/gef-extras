"""
Describe thoroughly what your command does. In addition, complete the documentation
in /docs/ and adding the reference in /mkdocs.yml
"""

__AUTHOR__ = "devtty1er"
__VERSION__ = 0.1
__LICENSE__ = "MIT"

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from . import *  # this will allow linting for GEF and GDB


@register
class MyCommand(GenericCommand):
    _cmdline_ = "printr"
    _syntax_ = "{:s}".format(_cmdline_)

    def pre_load(self) -> None:
        super().pre_load()

    def __init__(self) -> None:
        super().__init__(complete=gdb.COMPLETE_NONE)

    def post_load(self) -> None:
        super().post_load()

    def do_invoke(self, argv: List[str]):
        print("foo")