from abc import ABC, abstractmethod

"""
DIP Principe should depend on abstraction not on details!
"""


class Worker(ABC):
    @abstractmethod
    def work(self):
        pass


class DefaultWorker(Worker):
    def work(self):
        print("I'm working!!")


class SuperWorker(Worker):
    def work(self):
        print("I work very hard!!!")


class LazyWorker(Worker):
    def work(self):
        print("I'm a very lazy worker!")

class Manager:

    def __init__(self):
        self.workers = None

    def set_worker(self, worker):
        assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = DefaultWorker()
super_worker = SuperWorker()
lazy_worker = LazyWorker()

manager = Manager()

manager.set_worker(worker)
manager.manage()

manager.set_worker(lazy_worker)
manager.manage()

try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
