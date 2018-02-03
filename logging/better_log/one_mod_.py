import logging
import two_mod_ as two_mod


def main():
    """
    The main entry point of the application.
    :return: None
    """
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # Create the logging file handler
    fh = logging.FileHandler("better.log")

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)

    # Add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = two_mod.add(7, 8)
    logger.info("Done!")


if __name__ == "__main__":
    main()
