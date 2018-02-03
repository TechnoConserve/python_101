import configparser
import os


def create_config(path):
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


def crud_config(path):
    """
    Create, read, update, delete configuration options.
    :param path: File path to save output configuration file.
    :return: None
    """
    config = get_config(path)

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


def delete_setting(path, section, setting):
    """
    Delete a setting.
    :param path: File path to search for the configuration file.
    :param section: Name of the section heading in the config file.
    :param setting: Name of the setting to delete.
    :return: None
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    """
    Returns the config object.
    :param path: File path to search for the configuration file.
    :return: File object of the configuration file.
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    """
    Print out a setting.
    :param path: File path to search for the configuration file.
    :param section: Name of the section heading in the config file.
    :param setting: Name of the setting to check.
    :return: Value of the given setting.
    """
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )
    print(msg)
    return value


def update_setting(path, section, setting, value):
    """
    Update a setting.
    :param path: File path to search for the configuration file.
    :param section: Name of the section heading in the config file.
    :param setting: Name of the setting to update.
    :param value: Value to change the setting to.
    :return: None
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    font = get_setting(path, "Settings", "font")
    font_size = get_setting(path, "Settings", "font_size")

    update_setting(path, "Settings", "font_size", "12")

    delete_setting(path, "Settings", "font_style")
