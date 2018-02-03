import logging
import logging.config
import two_mod_


def main():
    """
    Based on  http://docs.python.org/howto/logging.html#configuring-logging
    :return: None
    """
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("exampleApp")

    logger.info("Program started")
    result = two_mod_.add(7, 8)
    logger.info("Done!")


if __name__ == "__main__":
    main()