import threading
from threading import Thread

class ClassName():
    def func1(self):
        print ('2')

    def func2(self):
        print ('3')

    def runall(self):
        if __name__ == '__main__':
            Thread(target = self.func1).start()
            Thread(target = self.func2).start()
run = ClassName()
run.runall() # will run all the def's in the same time