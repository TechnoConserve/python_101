import logging

module_logger = logging.getLogger("exampleApp.two_mod")


def add(x, y):
    """
    Add two numbers together.
    :param x: First number to be added.
    :param y: Second number to be added.
    :return: Return the sum of first and second numbers.
    """
    logger = logging.getLogger("exampleApp.two_mod.add")
    logger.info("added %s and %s to get %s" % (x, y, x + y))
    return x + y
