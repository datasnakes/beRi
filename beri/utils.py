import toml
from pkg_resources import resource_filename
from pathlib import Path
DEFAULT_CONFIG = resource_filename()  # TODO-ROB: After creating a proper module from cookies, use beRi_config.toml


def get_configuration(f):
    # Override default values with values from a file
    default_dict = toml.load(DEFAULT_CONFIG)
    if Path(f).is_file():
        new_dict = toml.load(f)
    # ***MAGIC***
    config_dict = {"default_dict": "merged with new dict created by file"}
    return config_dict
