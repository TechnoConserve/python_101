import configparser
import os


def createConfig(path):
    """
    Create a configuration file.
    :param path: File path to save output configuration file.
    :return: None
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info", "You are using %(font)s at %(font_size)s pt")

    with open(path, "w") as config_file:
        config.write(config_file)


def crudConfig(path):
    """
    Create, read, update, delete configuration options.
    :param path: File path to save output configuration file.
    :return: None
    """
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    # Read some values from the config
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")

    # Change a value in the config
    config.set("Settings", "font_size", "12")

    # Delete a value from the config
    config.remove_option("Settings", "font_style")

    # Write changes back to the config file
    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    crudConfig(path)
