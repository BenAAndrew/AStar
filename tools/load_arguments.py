import argparse
import configparser

arguments = None
config = None

# Config constants
FILENAME = "astar.ini"
SECTIONS = {"Visual": ["Size", "Speed"], "Colours": ["EMPTY", "WALL"]}


def load_arguments():
    global arguments, config

    # Load command line arguments
    parser = argparse.ArgumentParser(description="Show the A* processing and optimal path for a defined maze")
    parser.add_argument("-f", type=str, help="File name & path (i.e. mazes/maze1.txt)")
    parser.add_argument("-s", type=int, help="Screen size in pixels (i.e. 400 -> 400x400 screen)")
    arguments = vars(parser.parse_args())

    # Load config values
    config = configparser.ConfigParser()
    config.read(FILENAME)

    # Validate config values
    assert config.sections(), "No config file found. See example config file for this"
    for section, variables in SECTIONS.items():
        assert section in config, f"Section {section} not found in config file"
        for variable in variables:
            assert variable in config[section], f"Value for {variable} not defined"


def get_config_value(section, name):
    value = config[section][name]
    if "." in value:
        return float(value)
    elif "," in value:
        return [int(num) for num in value.split(",")]
    else:
        return int(value)


def get_command_line_argument(name):
    return arguments[name]


def get_screen_size():
    if "s" in arguments:
        return arguments["s"]
    else:
        return int(config["Visual"]["Size"])
