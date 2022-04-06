import sys
import textwrap
import yaml
from typing import Callable, TypeVar

__all__ = [
    "Assets",
    "load_config",
    "modify_vars",
]

T = TypeVar("T")


def load_config(file_path: str):
    """
    Loads configuration as a `dict` from a `.yaml` file

    Apply decorator to a function whose first positional argument
    is a config of type `dict`

    ## Example:
    ```python
    @load_config("../config/config.yaml")
    def main(config: dict, ...):
        pass
    ```

    ---

    - @param file_path: str [ Path to .yaml configuration file]
    """

    config_data = yaml.safe_load(open(file_path, "r"))

    def outer(func: Callable[[dict], None]):

        def inner():
            return func(config_data)
        return inner
    return outer


def modify_vars(cls: T, func: Callable, *f_args, **f_kwargs):
    """
    Calls passed function on all user-defined members of a class

    - @param cls: T [ Class to modify ]
    - @param func: Callable [ Function to call of members ]
    - @param f_args: Any [ Positional arguments to pass to function ]
    - @param f_kwargs: Any [ Keyword arguments to pass to function ]
    """

    # Get all variables
    filtered_members = filter(lambda f: not f.startswith("__"), vars(cls))

    # Extract member names and values
    for member in filtered_members:
        attr = getattr(cls, member)
        setattr(cls, member, func(attr, *f_args, **f_kwargs))


class Assets:
    class Styles:
        background = """\
        QLabel {
            background-color: coral;
        }
        """

        poly_box_container = """\
        QLabel {
            background-color: 
        }
        """


# Unindent each member
# This isn't necessary but makes reading output cleaner
modify_vars(Assets.Styles, textwrap.dedent)
