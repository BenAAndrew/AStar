import configparser

FILENAME = "astar.ini"
SECTIONS = {"Visual": ["Width", "Speed"], "Colours": ["EMPTY", "WALL"]}

# Load Config
config = configparser.ConfigParser()
config.read(FILENAME)

# Validate
assert config.sections(), "No config file found. See example config file for this"
for section, variables in SECTIONS.items():
    assert section in config, f"Section {section} not found in config file"
    for variable in variables:
        assert variable in config[section], f"Value for {variable} not defined"

# Function
def get_value(section, name):
    value = config[section][name]
    if "." in value:
        return float(value)
    elif "," in value:
        return [int(num) for num in value.split(",")]
    else:
        return int(value)
