import logging
import two_mod


def main():
    """
    The main entry point of the application.
    :return: None
    """
    logging.basicConfig(filename="multi_mod.log", level=logging.INFO)
    logging.info("Program started")
    result = two_mod.add(7, 8)
    logging.info("Done!")


if __name__ == "__main__":
    main()
