# Exemple 6 : Salut Toto
# À l’aide de deux threads, écrire “Salut Toto Salut Toto Salut Toto”, sachant que le premier
# thread écrit “Salut” et que le deuxième écrit “Toto”.

# Create 2 threads that are using a rare resource.
# Each thread has to acquire the resource before he can use it.
# After using the resource, the thread release the resource, then politely waits to benotified by another thread.
# As soon as it wakes, up, the thread grabs the resource again...

from threading import Thread
from threading import Condition
import logging

class ProtectedResource(Condition):
    """This is the rare resource that performs rare work.
        Actually it just prints a name.   
    """
    def rare_work(self, name: str):
        print(name, end=" ")


class SimpleThread(Thread):

    resource: ProtectedResource
    loops: int

    def __init__(self, name:str, loops: int, resource: Condition):
        """ Creates a thread that will perform 'loops' iterations.
            During each iteration the thread will acquire the lock on the resource,
            perform rare work (print the string passed in the 'name' argument),
            then release the resource and then wait until it gets notified by another thread.
        """
        super().__init__(name=name)
        self.resource = resource
        self.loops = loops

    def run(self) -> None:
        # Acquire the resource
        logging.debug("Init - Acquiring the resource...")
        self.resource.acquire()
        for i in range(self.loops):
            logging.debug("Iteration {} - Acquired the resource.".format(i))
            # Do the important work
            resource.rare_work(self.name)
            # Notify other waiting threads and give them a chance to grab the resource
            self.resource.notify_all()
            if i < (self.loops - 1):
                # This is NOT the last iteration => release the resources,
                # wait until another thread notifies me, then grab the resource again.
                logging.debug("Iteration {} - Releasing the resource, then waiting...".format(i))
                self.resource.wait()
                # The Thread.wait() method returns only after another thread has notified this one,
                # and the resource becomes available again.
            else:
                # This is the last iteration => just release the resource
                self.resource.release()
                logging.debug("Iteration {} - Released the resource for the last time.".format(i))
        logging.debug("Reached the end of the run() method.".format(self.name))

logging.basicConfig(format="%(asctime)s[%(threadName)s]%(levelname)s:%(message)s", level=logging.INFO)
resource = ProtectedResource()
t1 = SimpleThread(name="Salut", loops=10 , resource=resource)
t2 = SimpleThread(name="Toto", loops=10, resource=resource)
t1.start()
t2.start()
