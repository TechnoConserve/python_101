import random
import time

from threading import Thread


class MyThread(Thread):
    """
    A threading example.
    """

    def __init__(self, name):
        """Initialize the thread"""
        Thread.__init__(self)
        self.name = name

    def run(self):
        """Run the thread"""
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = '{} is running'.format(self.name)
        print(msg)


def create_threads():
    """
    Create a group of threads.
    :return: None
    """
    for i in range(1, 6):
        name = "Thread #{}".format(i)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == '__main__':
    create_threads()
