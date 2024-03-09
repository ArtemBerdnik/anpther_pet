import configparser
import os


def get_properties(value: str) -> str:
    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_directory, "..", "properties.ini")

    config = configparser.RawConfigParser()
    config.read(config_path)
    return config['DEFAULT'][value]


class PropertiesHandler:
    pass
