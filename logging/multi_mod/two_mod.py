import logging


def add(x, y):
    """
    Add two numbers together.
    :param x: First number to be added.
    :param y: Second number to be added.
    :return: Return the sum of first and second numbers.
    """
    logging.info("Added {first} and {second} to get {total}"
                 .format(first=x, second=y, total=x + y))
